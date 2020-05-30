# flake8: noqa
import _pytest.mark
import pytest

unit: _pytest.mark.MarkDecorator = pytest.mark.unit
asyncio: _pytest.mark.MarkDecorator = pytest.mark.asyncio
