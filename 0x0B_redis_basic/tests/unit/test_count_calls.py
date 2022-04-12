def test_count_calls(f__cache):
    cache = f__cache

    cache.store(b"First")
    assert cache.get(cache.store.__qualname__) == b"1"

    cache.store(b"Second")
    assert cache.get(cache.store.__qualname__) == b"2"

    cache.store(b"Third")
    assert cache.get(cache.store.__qualname__) == b"3"
