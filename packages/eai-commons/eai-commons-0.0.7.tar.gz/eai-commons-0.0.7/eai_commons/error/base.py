from copy import deepcopy
from typing import Optional, Any
from pydantic import BaseModel, Field


class Error(BaseModel):
    code: str = Field(alias="code")
    message: str = Field(alias="message")
    details: Optional[dict[str, Any]] = Field(alias="details", default=None)

    def to_error_body(self):
        return {"error": self.dict(by_alias=True)}

    def format(self, **kwargs):
        e_ = deepcopy(self)
        e_.message = e_.message.format(**kwargs)
        return e_


class ErrorCodeException(Exception):
    """内部异常类"""

    def __init__(self, error: Error, code: int = 400, details: Any = None):
        self.error = error
        self.code = code
        self.details = details
