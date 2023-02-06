#!/usr/bin/env python3
"""The basics of async"""


import asyncio
import random

async def wait_random(max_delay: int = 10.0) -> float:
    """
    an asynchronous coroutine that takes in an integer argument
    max_delay (int)
    waits for a random delay between 0 and max_delay seconds
    and eventually returns it.
    """
    rand_delay = random.uniform(0, float(max_delay))
    await asyncio.sleep(rand_delay)
    return rand_delay
