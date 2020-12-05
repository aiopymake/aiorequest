"""Package provides asynchronous user-friendly HTTP client with clean objects."""
from typing import Tuple
from aiorequest.types import Credentials
from aiorequest.responses import JsonType, Response, ResponseError, safe_response
from aiorequest.sessions import HttpSession, LoggedHttpSession, Session
from aiorequest.urls import Address, HttpUrl, HttpsUrl, Url

__author__: str = "Volodymyr Yahello"
__email__: str = "vyahello@gmail.com"
__license__: str = "MIT"
__copyright__: str = f"Copyright 2020, {__author__}"
__version__: str = "0.0.2"

__all__: Tuple[str, ...] = (
    "Credentials",
    "Session",
    "HttpSession",
    "LoggedHttpSession",
    "JsonType",
    "Response",
    "ResponseError",
    "safe_response",
    "Address",
    "HttpUrl",
    "HttpsUrl",
    "Url",
)
