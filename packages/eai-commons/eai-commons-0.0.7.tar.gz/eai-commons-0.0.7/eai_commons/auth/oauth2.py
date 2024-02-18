import requests
from abc import abstractmethod

from eai_commons.logging import logger
from eai_commons.error.errors import ForbiddenException, UNAUTHORIZED


def _verify_request_success(response: requests.Response) -> None:
    if response.status_code != 200:
        logger.error(
            f"access error. url = {response.request.url}, "
            f"http code = {response.status_code}, error msg = {response.text}"
        )
        raise ForbiddenException(UNAUTHORIZED)


class OAuth2Service:
    @abstractmethod
    def authcode_to_access_token(self, authcode: str):
        raise NotImplementedError

    @abstractmethod
    def access_token_to_userinfo(self, access_token: str):
        raise NotImplementedError
