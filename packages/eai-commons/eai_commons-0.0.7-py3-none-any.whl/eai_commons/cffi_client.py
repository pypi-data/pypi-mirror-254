import asyncio
import httpx

from typing import Optional, AsyncIterator, Any, Callable
from concurrent.futures.thread import ThreadPoolExecutor
from httpx import Timeout
from curl_cffi.requests import AsyncSession


FINISHED = object()
REQUEST_EXECUTORS = ThreadPoolExecutor(8)


async def stream_request(
    method: str,
    url: str,
    headers,
    body,
    proxies: Optional[dict[str, str]] = None,
    impersonate: Optional[str] = None,
    timeout: int = 60,
) -> AsyncIterator[dict[str, Any]]:
    if impersonate:
        queue = asyncio.Queue()
        printer = CallbackPrinter(queue=queue)
        asyncio.get_event_loop().run_in_executor(
            REQUEST_EXECUTORS,
            cffi_request,
            method,
            url,
            headers,
            body,
            proxies,
            impersonate,
            printer.write,
        )

        async for resp in printer.get_data():
            yield resp

        return

    async with httpx.AsyncClient(
        proxies=proxies,
        timeout=Timeout(timeout=float(timeout)),
    ) as client:
        async with client.stream(method, url, headers=headers, data=body) as response:
            buffer = b""
            async for chunk in response.aiter_bytes():
                buffer += chunk
                if response.status_code != 200:
                    yield chunk
                    return

                while b"\n" in buffer:
                    event, buffer = buffer.split(b"\n", 1)
                    yield event + b"\n"


async def async_request(
    method: str,
    url: str,
    headers: Optional[dict[str, str]] = None,
    params: Optional[dict] = None,
    json_: Optional[dict] = None,
    proxies: Optional[dict[str, str]] = None,
    impersonate: Optional[str] = None,
    timeout: int = 60,
) -> httpx.Response:
    if impersonate:
        cffi_proxies = None
        if proxies is not None:
            cffi_proxies = {
                "https": proxies.get("https://"),
                "http": proxies.get("http://"),
            }

        async with AsyncSession() as async_session:
            return await async_session.request(
                method,
                url=url,
                headers=headers,
                params=params,
                json=json_,
                proxies=cffi_proxies,
                impersonate=impersonate,
            )

    async with httpx.AsyncClient(
        proxies=proxies, timeout=Timeout(timeout=float(timeout))
    ) as client:
        return await client.request(
            method, url, headers=headers, params=params, json=json_
        )


def cffi_request(
    method: str,
    url: str,
    headers,
    body: Optional[bytes] = None,
    proxies: Optional[dict[str, str]] = None,
    impersonate: Optional[str] = "chrome110",
    callback: Optional[Callable] = None,
):
    cffi_proxies = None
    if proxies is not None:
        cffi_proxies = {
            "https": proxies.get("https://"),
            "http": proxies.get("http://"),
        }
    from curl_cffi import requests

    try:
        requests.request(
            method,
            url=url,
            headers=headers,
            data=body,
            proxies=cffi_proxies,
            impersonate=impersonate,
            content_callback=callback,
        )
    finally:
        callback(FINISHED)


class CallbackPrinter:
    queue: asyncio.Queue = None

    def __init__(self, queue):
        self.queue = queue

    def write(self, value):
        self.queue.put_nowait(value)

    async def get_data(self):
        while True:
            try:
                data = await asyncio.wait_for(self.queue.get(), 300)
                if data == FINISHED:
                    break

                yield data
            except Exception as e:
                print(e)
                break
