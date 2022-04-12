import pytest


@pytest.mark.parametrize(
    "data,expected",
    [
        ("First", [b"('First',)"]),
        ("Second", [b"('Second',)"]),
        ("Third", [b"('Third',)"])
    ]
)
def test_call_history(data, expected, f__cache):
    cache = f__cache

    key = cache.store(data)
    inputs = cache._redis.lrange(f"{cache.store.__qualname__}:inputs", 0, -1)
    outputs = cache._redis.lrange(f"{cache.store.__qualname__}:outputs", 0, -1)

    assert inputs == expected
    assert outputs == [key.encode("utf-8")]
