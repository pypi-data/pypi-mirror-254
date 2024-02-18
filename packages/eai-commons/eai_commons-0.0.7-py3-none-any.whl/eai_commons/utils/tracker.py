import time
import typing as t
import functools
from inspect import iscoroutinefunction

from eai_commons.utils.func import get_compact_function_name
from eai_commons.utils.time import current_timestamp, to_date_string, DATE_TIME_PATTERN
from eai_commons.logging import logger


class Timer:
    def __init__(self, desc: str = None):
        self._start_time = None
        self._desc = desc

    def __enter__(self):
        self._start_time = time.perf_counter()

    def __exit__(self, type, value, traceback):
        elapsed_time = time.perf_counter() - self._start_time
        logger.info(f"{self._desc} elapsed time: {elapsed_time:0.4f} seconds")

        self._start_time = None


def time_spend(*dargs: t.Any):
    """
    计算函数执行时间，以日志形式记录。
    """
    if len(dargs) == 1 and callable(dargs[0]):
        return time_spend()(dargs[0])
    else:

        def decorator(func):
            origin_function_name = get_compact_function_name(func)

            if iscoroutinefunction(func):

                @functools.wraps(func)
                async def async_wrapper(*args, **kwargs):
                    begin = current_timestamp()
                    try:
                        return await func(*args, **kwargs)
                    except Exception as e:
                        raise e
                    finally:
                        end = current_timestamp()
                        logger.info(
                            f"func=[{origin_function_name}], spend time: {end - begin}ms, "
                            f"start at: [{to_date_string(begin, DATE_TIME_PATTERN)}]"
                        )

                return async_wrapper
            else:

                def wrapper(*args, **kwargs):
                    begin = current_timestamp()
                    try:
                        return func(*args, **kwargs)
                    except Exception as e:
                        raise e
                    finally:
                        end = current_timestamp()
                        logger.info(
                            f"func=[{origin_function_name}], spend time: {end - begin}ms, "
                            f"start at: [{to_date_string(begin, DATE_TIME_PATTERN)}]"
                        )

                return wrapper

        return decorator
