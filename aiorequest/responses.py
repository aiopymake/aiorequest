"""The module contains a set of API for HTTP responses types."""
from typing import Iterable
import http
import requests
from punish import AbstractStyle, abstractstyle
from aiorequest.types import AnyUnionDict

JsonType = AnyUnionDict
HTTPStatus = http.HTTPStatus


class ResponseError(Exception):
    """The class represents HTTP api request response error."""

    pass


class Response(AbstractStyle):
    """The class represents an abstraction of a response from an API request."""

    @abstractstyle
    async def is_ok(self) -> bool:
        """Returns `True` if response is `OK` otherwise `False`."""
        pass

    @abstractstyle
    async def status(self) -> HTTPStatus:
        """Returns HTTP response status."""
        pass

    @abstractstyle
    async def as_json(self) -> JsonType:
        """Returns HTTP response data as dictionary type."""
        pass

    @abstractstyle
    async def as_str(self) -> str:
        """Returns HTTP response data as plain data type."""
        pass


class HttpResponse(Response):
    """The class represents an HTTP response from HTTP API request."""

    def __init__(self, response: requests.Response) -> None:
        self._response: requests.Response = response

    async def is_ok(self) -> bool:
        """See base class."""
        return self._response.ok

    async def status(self) -> HTTPStatus:
        """See base class."""
        return HTTPStatus(self._response.status_code)

    async def as_json(self) -> JsonType:
        """See base class."""
        return self._response.json()

    async def as_str(self) -> str:
        """See base class."""
        return self._response.text


async def safe_response(
    response: Response,
    success_codes: Iterable[int] = (HTTPStatus.OK, HTTPStatus.CREATED, HTTPStatus.NO_CONTENT),
) -> Response:
    """Specifies safe response from iterable of success HTTP status codes.

    Args:
        response: a specific HTTP response
        success_codes: a list of allowed success codes

    Raises:
        `ResponseError` if HTTP response contains a set of errors
    Returns: a response
    """
    if await response.status() not in success_codes:
        raise ResponseError(
            f"HTTP response contains some errors with '{await response.status()}' status! "
            f"Reason: {await response.as_str()}"
        )
    return response
