#!/usr/bin/env python3
"""
multiple coroutines at the same time with async
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Args:
        n: first float
        max_delay: second float
    Returns:
        the list of all delays in asecending order
    """
    steps = []
    delays = []

    for i in range(n):
        steps.append(asyncio.create_task(wait_random(max_delay)))

    for step in asyncio.as_completed(steps):
        delays.append(await step)
    return delays
