from exercise import Cache
import pytest
from typing import List


@pytest.mark.parametrize(
    "data,expected",
    [
        ("First", [b"('First',)"]),
        ("Second", [b"('Second',)"]),
        ("Third", [b"('Third',)"])
    ]
)
def test_call_history(
    data: str,
    expected: List[bytes],
    f__cache: pytest.fixture
):
    cache: Cache = f__cache

    key: str = cache.store(data)
    inputs: List[bytes] = cache._redis.lrange(
        f"{cache.store.__qualname__}:inputs", 0, -1
    )
    outputs: List[bytes] = cache._redis.lrange(
        f"{cache.store.__qualname__}:outputs", 0, -1
    )

    assert inputs == expected
    assert outputs == [key.encode("utf-8")]
