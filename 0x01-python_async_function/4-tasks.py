#!/usr/bin/env python3
"""
Tasks - 4
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
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
        steps.append(task_wait_random(max_delay))

    for step in asyncio.as_completed(steps):
        delays.append(await step)
    return delays
