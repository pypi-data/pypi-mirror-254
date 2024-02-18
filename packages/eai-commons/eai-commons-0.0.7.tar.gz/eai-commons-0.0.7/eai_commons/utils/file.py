import os
import json
import tempfile
import fcntl

from typing import Optional


def file_relative_path(dunderfile: str, relative_path: str) -> str:
    """
    Return the relative path of a file to another file.

    Example:
        ``path_ = file_relative_path(__file__, "../error/errors.py")``

        You can get the absolute path from path.py to errors.py.
    """
    return os.path.join(os.path.dirname(dunderfile), relative_path)


def get_file_extension(file: str) -> str:
    """
    Return the extension of a file.

    Example:
        ``extension = get_file_extension("/opt/code/file.py")``

        The extension is ``.py``
    """
    return os.path.splitext(file)[1].lower()


def load_json_file(path: str) -> list | dict:
    """
    Load a json file.

    Example:
        ``data = load_json_file("/opt/code/file.json")``
    """
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def create_dir_if_not_existed(directory_path: str, lockfile: Optional[str] = None):
    """
    目录存在，默认跳过。创建目录，通过加锁机制，避免多进程下并发创建失败的问题
    :param directory_path: 目录的绝对地址
    :param lockfile: 锁路径，默认为临时目录下的.eai_commons.lock
    :return:
    """
    if os.path.exists(directory_path):
        return

    if lockfile is None:
        lockfile = f"{tempfile.gettempdir()}/.eai_commons.lock"

    with open(lockfile, "w") as lockfile:
        fcntl.flock(lockfile, fcntl.LOCK_EX)
        try:
            os.makedirs(directory_path, exist_ok=True)
        except FileExistsError:
            pass
        finally:
            fcntl.flock(lockfile, fcntl.LOCK_UN)
