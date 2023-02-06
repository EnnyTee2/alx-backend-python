#!/usr/bin/env python3
'''
Executing multiple coroutines simultaneosly with async
'''
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int):
    """
    Measures the total execution time for the wait_n function
    """
    start = time.perf_counter()
    wait_n(n, max_delay)
    total_time = time.perf_counter() - start

    return (total_time / n)
