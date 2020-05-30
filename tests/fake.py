from http import HTTPStatus
from aiorequest.responses import JsonType, Response


class FakeHttpResponse(Response):
    """The class represents fake HTTP response interface."""

    def __init__(
        self, code: HTTPStatus, is_ok: bool = True, as_str: str = str(), as_dict: JsonType = {}
    ) -> None:
        self._code: HTTPStatus = code
        self._is_ok: bool = is_ok
        self._as_str: str = as_str
        self._as_dict: JsonType = as_dict

    async def is_ok(self) -> bool:
        return self._is_ok

    async def code(self) -> HTTPStatus:
        return self._code

    async def as_json(self) -> JsonType:
        return self._as_dict

    async def as_str(self) -> str:
        return self._as_str
