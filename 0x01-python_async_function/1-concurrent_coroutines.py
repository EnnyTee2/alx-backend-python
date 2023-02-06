#!/usr/bin/env python3
'''
Executing multiple coroutines simultaneosly with async
'''
import asyncio


wait_random = __import__('0-basic_async_syntax.py').wait_random

async def wait_n(n: int, max_delay: int):
    delay_list = []
    for _ in range(n):
        a = await wait_random(max_delay)
        delay_list.append(a)
    return delay_list
    
