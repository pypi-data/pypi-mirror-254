import json
import zlib
import uuid
import csv

from io import StringIO


class ForceSerializableEncoder(json.JSONEncoder):
    def default(self, obj):
        try:
            from pydantic import BaseModel

            if isinstance(obj, BaseModel):
                return obj.json()
            return super().default(obj)
        except TypeError:
            # Skip non-serializable objects
            return None


def random_id(upper: bool = False, with_hypper: bool = False) -> str:
    """
    new_id
    :param upper: 是否大写
    :param with_hypper: 是否包含 -
    :return:
    """
    id_ = uuid.uuid4().__str__()
    if upper:
        id_ = id_.upper()
    if not with_hypper:
        id_ = id_.replace("-", "")
    return id_


def mask_string_position(s_, start: int, end: int, mask_char="*") -> str:
    """
    对一个长字符串打星号
    :param s_: 待处理的字符串
    :param start: 需要打星号的起始位置
    :param end: 需要打星号的结束位置
    :param mask_char: 星号字符，默认为 *
    :return: 处理后的字符串
    """

    assert start < end, "start should be less than end"
    assert start >= 0, "start should be greater than 0"
    assert end <= len(s_), "end should be less than the length of s_"

    return s_[:start] + mask_char * (end - start) + s_[end:]


def mask_string(
    s_,
    pre_no_mask: int,
    suf_no_mask: int,
    mask_char: str = "*",
    safety_mask: bool = True,
) -> str:
    """
    对一个长字符串打星号
    :param s_: 待处理的字符串
    :param pre_no_mask: 前面n个不需打码
    :param suf_no_mask: 后面n个不需打码
    :param mask_char: 星号字符，默认为 *
    :param safety_mask: 如果显示的字符数大于等于字符长度，则全部mask
    :return: 处理后的字符串
    """

    assert pre_no_mask >= 0, "pre_no_mask should be greater than 0"
    assert suf_no_mask >= 0, "suf_no_mask should be greater than 0"

    size = len(s_)
    if (
        pre_no_mask >= size
        or suf_no_mask >= size
        or (pre_no_mask + suf_no_mask) >= size
    ):
        return mask_char * size if safety_mask else s_
    end = size - suf_no_mask
    return s_[:pre_no_mask] + mask_char * (end - pre_no_mask) + s_[end:]


def compress(data: str, encoding: str = "utf-8") -> bytes:
    """
    字符串压缩为字节
    """
    byte_ = data.encode(encoding)
    length_before_compression = int.to_bytes(len(byte_), 4, "little")
    return length_before_compression + zlib.compress(byte_)


def decompress(body: bytes, encoding: str = "utf-8") -> str:
    """
    字节解压为字符串
    """
    return zlib.decompress(body[4:]).decode(encoding)


def split_chunks(input_string: str, chunk_size: int) -> list[str]:
    return [input_string[i:i + chunk_size] for i in range(0, len(input_string), chunk_size)]


def json_load(text: str) -> dict | list:
    """会自动忽略不合理的字符"""
    try:
        return json.loads(text)
    except json.JSONDecodeError as e:
        if e.doc[e.pos] in ("\\", "\n"):
            return json_load(e.doc[: e.pos] + e.doc[e.pos + 1 :])
        else:
            raise


def remove_illegal_characters(s):
    if isinstance(s, str):
        # 定义非法字符集合，这里包括了大部分控制字符
        illegal_chars = {chr(i) for i in range(32)}  # ASCII 码 0-31
        illegal_chars.remove("\t")  # 保留水平制表符
        illegal_chars.remove("\n")  # 保留换行符
        illegal_chars.remove("\r")  # 保留回车符

        # 移除字符串中的非法字符
        for illegal_char in illegal_chars:
            s = s.replace(illegal_char, "")
    return s
