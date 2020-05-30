from http import HTTPStatus
from typing import Iterable
import pytest
from tests.fake import FakeHttpResponse
from aiorequest.responses import Response, ResponseError, safe_response
from tests.markers import asyncio, unit

pytestmark = [unit, asyncio]


@pytest.mark.parametrize(  # noqa: PT006, PT007
    "code, expected",
    (
        pytest.param(
            HTTPStatus.CONTINUE,
            (HTTPStatus.CONTINUE, HTTPStatus.SWITCHING_PROTOCOLS, HTTPStatus.PROCESSING),
            id="info",
        ),
        pytest.param(
            HTTPStatus.OK,
            (HTTPStatus.OK, HTTPStatus.CREATED, HTTPStatus.UNAVAILABLE_FOR_LEGAL_REASONS),
            id="success",
        ),
        pytest.param(
            HTTPStatus.MULTIPLE_CHOICES,
            (HTTPStatus.MULTIPLE_CHOICES, HTTPStatus.MOVED_PERMANENTLY, HTTPStatus.FOUND),
            id="redirect",
        ),
        pytest.param(
            HTTPStatus.BAD_REQUEST,
            (HTTPStatus.BAD_REQUEST, HTTPStatus.UNAUTHORIZED, HTTPStatus.PAYMENT_REQUIRED),
            id="client error",
        ),
        pytest.param(
            HTTPStatus.INTERNAL_SERVER_ERROR,
            (HTTPStatus.INTERNAL_SERVER_ERROR, HTTPStatus.NOT_IMPLEMENTED, HTTPStatus.BAD_GATEWAY),
            id="server error",
        ),
    ),
)
async def test_safe_response_code(code: HTTPStatus, expected: Iterable[int]) -> None:
    assert isinstance(await safe_response(FakeHttpResponse(code), success_codes=expected), Response)


async def test_safe_response_error() -> None:
    with pytest.raises(ResponseError):
        await safe_response(
            FakeHttpResponse(HTTPStatus.INTERNAL_SERVER_ERROR),
            success_codes=(HTTPStatus.OK, HTTPStatus.CREATED),
        )


async def test_response_as_json(response: Response) -> None:
    assert await response.as_json()


async def test_response_is_ok(response: Response) -> None:
    assert await response.is_ok()


async def test_response_code(response: Response) -> None:
    assert await response.code() is HTTPStatus.OK


async def test_response_text(response: Response) -> None:
    assert await response.as_str()


async def test_logged_response_as_json(logged_response: Response) -> None:
    assert await logged_response.as_json()


async def test_logged_response_is_ok(logged_response: Response) -> None:
    assert await logged_response.is_ok()


async def test_logged_response_code(logged_response: Response) -> None:
    assert await logged_response.code() is HTTPStatus.OK


async def test_logged_response_text(logged_response: Response) -> None:
    assert await logged_response.as_str()
