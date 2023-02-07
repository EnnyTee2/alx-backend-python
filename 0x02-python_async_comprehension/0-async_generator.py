#!/usr/bin/env python3
'''Task 0 - Async Generator'''


import random
import asyncio


async def async_generator():
    """
    A coroutine that loops 10 times, each time asynchronously wait 1 second,
    then yields a random number between 0 and 10.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.randrange(1, 10)
