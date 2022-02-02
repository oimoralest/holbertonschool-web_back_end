#!/usr/bin/env python3
"""
2. Measure the runtime
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Args:
        n: first float
        max_delay: second float
    Returns:
        total time / n as float
    """
    time_starts = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    time_ends = time.perf_counter()
    time_elapsed = time_ends - time_starts

    return time_elapsed / n
