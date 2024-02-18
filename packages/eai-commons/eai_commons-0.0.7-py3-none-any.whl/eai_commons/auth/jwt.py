import jwt

from copy import deepcopy
from datetime import datetime
from jwt.exceptions import PyJWTError

from eai_commons.logging import logger
from eai_commons.error.errors import (
    ForbiddenException,
    UNAUTHORIZED,
)


class Jwt:
    sha256_secret: str
    expired: int
    leeway: int
    exp_claim = "exp"

    def __init__(
        self, sha256_secret: str, expired: int = 60 * 60 * 24, leeway: int = 10
    ):
        self.sha256_secret = sha256_secret
        self.expired = expired
        self.leeway = leeway

    def create_jwt(self, payload: dict) -> str:
        """
        基于payload 生成jwt token
        """
        encode_mapping = deepcopy(payload)
        # 设置 x 秒的过期时间
        encode_mapping[self.exp_claim] = datetime.now().timestamp() + self.expired
        return jwt.encode(encode_mapping, self.sha256_secret, algorithm="HS256")

    def verify_jwt(self, jwt_token: str) -> dict:
        """
        校验jwt是否合法。
        1.内嵌过期时间。
        """
        try:
            decode = jwt.decode(
                jwt_token, self.sha256_secret, leeway=self.leeway, algorithms="HS256"
            )
            decode.pop(self.exp_claim)
            return decode
        except PyJWTError as e:
            logger.warning(f"decode jwt token occur error: {e}")
            raise ForbiddenException(UNAUTHORIZED)
