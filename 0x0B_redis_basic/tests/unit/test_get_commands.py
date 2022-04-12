"""Defines tests for get method"""
from exercise import Cache
from typing import Callable, Union
import pytest


@pytest.mark.parametrize(
    "data,callable",
    [
        # Test get method with bytes and None callable
        (b"foo", None),
        # Test get method with int and int callable
        (123, int),
        # Test string with custom callable
        ("bar", lambda d: d.decode("utf_8"))
    ]
)
def test_get(
    data: Union[str, int, bytes, float],
    callable: Callable,
    f__cache: pytest.fixture
):
    cache: Cache = f__cache
    key: str = cache.store(data)

    assert cache.get(key, callable) == data
