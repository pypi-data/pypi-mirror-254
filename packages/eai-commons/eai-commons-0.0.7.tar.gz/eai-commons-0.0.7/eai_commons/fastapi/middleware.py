import time
import ipaddress
import typing
import shortuuid

from starlette.requests import Request
from starlette.responses import Response
from starlette.middleware.base import BaseHTTPMiddleware, DispatchFunction
from starlette.types import ASGIApp

from eai_commons import trace_id_context
from eai_commons.logging import logger
from eai_commons.error.errors import (
    ForbiddenException,
    ACCESS_DENY_ERROR,
)


class IPAccessControlMiddleware(BaseHTTPMiddleware):
    def __init__(
        self,
        app: ASGIApp,
        allow_ip_list: list[str],
        intranet_pass: bool = True,
        black_ip_list: list[str] = None,
        dispatch: typing.Optional[DispatchFunction] = None,
    ) -> None:
        """
        allow_ip_list: 在此列表的IP放行，必须配置。
        intranet_pass: 内网ip默认放行。否则需要配置在allow_ip_list中。
        black_ip_list: 在此列表的，无论内外网，都被block。
        """
        self.allow_ip_list = allow_ip_list
        self.intranet_pass = intranet_pass
        self.black_ip_list = black_ip_list

        super().__init__(app, dispatch)

    async def dispatch(self, request: Request, call_next) -> Response:
        real_ip = request.headers.get("X-Real-IP")
        if not self._allow_access(real_ip):
            print(f"access deny from {real_ip}")
            raise ForbiddenException(ACCESS_DENY_ERROR)

        start_time = time.time()
        response = await call_next(request)
        end_time = time.time()
        response_time = end_time - start_time

        logger.info(
            f"{request.headers.get('X-Real-IP')} {request.client.host}:{request.client.port} - "
            f"{response.status_code} {response_time * 1000:.2f}ms"
        )

        return response

    def _allow_access(self, ip: str) -> bool:
        # x-real-ip 为None，说明是内部请求
        if ip is None:
            return True

        address = ipaddress.ip_address(ip)

        if self.black_ip_list and ip in self.black_ip_list:
            return False

        # 私有 IP 放通
        if address.is_private and self.intranet_pass:
            return True

        if ip in self.allow_ip_list:
            return True

        return False


class HttpAccessMiddleware(BaseHTTPMiddleware):
    @staticmethod
    def get_path_with_query_string(request: Request) -> str:
        if request.url.query:
            return f"{request.url.path}?{request.url.query}"
        return request.url.path

    async def dispatch(self, request: Request, call_next) -> Response:
        trace_id = shortuuid.uuid()
        trace_id_context.set(trace_id)

        start_time = time.time()
        response = await call_next(request)
        end_time = time.time()
        response_time = end_time - start_time

        remote_ip = request.headers.get("X-Real-IP") or "N/A"

        logger.info(
            f"{remote_ip} - "
            f"{request.client.host}:{request.client.port} - "
            f'"{request.method} {HttpAccessMiddleware.get_path_with_query_string(request)}" '
            f"{response.status_code} {response_time * 1000:.2f}ms"
        )

        response.headers["x-tr"] = trace_id
        return response
