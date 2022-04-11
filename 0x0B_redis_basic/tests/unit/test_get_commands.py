"""Defines tests for get method"""
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
def test_get(data, callable, f__cache):
    cache = f__cache
    key = cache.store(data)

    assert cache.get(key, callable) == data
