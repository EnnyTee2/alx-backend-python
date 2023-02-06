#!/usr/bin/env python3
"""The basics of async"""


import asyncio
import random

async def wait_random(max_delay: float = 10.0) -> float:
    rand_delay = random.randrange(0, max_delay)
    asyncio.sleep(rand_delay)
    return rand_delay
    
