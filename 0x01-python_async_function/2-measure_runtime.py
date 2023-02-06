#!/usr/bin/env python3
'''
Executing multiple coroutines simultaneosly with async
'''
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int):
    start = time.perf_counter()
    wait_n(n, max_delay)

    return time.perf_counter() - start
