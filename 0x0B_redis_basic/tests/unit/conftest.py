import pytest
from exercise import Cache


@pytest.fixture()
def f__cache() -> Cache:
    """Creates an instance of Cache class"""
    return Cache()
