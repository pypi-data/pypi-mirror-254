#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
Execute functions with multithreading.

Functions must accept the iterator, and other arguments as a dictionary.
See test_function() and main() for usage example.

Returns the list of results from all executions.
"""
from concurrent import futures as cf
from typing import Callable
from time import sleep
import sys


__version__ = '1.0.3'


def threads(
    function_name: Callable,
    iterators: list,
    items: dict,
    thread_num: int = 10
) -> list:
    """Execute functions with multithreading."""
    with cf.ThreadPoolExecutor(max_workers=thread_num) as executor:
        results = []
        for iterator in iterators:
            future = executor.submit(
                function_name,
                iterator,
                items
            )
            results.append(future)
    return [result.result() for result in results]


def test_function(
    iterator,
    items
) -> int:
    """Sum two numbers."""
    print(iterator)
    sleep(1)
    return items['a'] + items['b']


def main():
    """
    Test multithreading.
    
    The number of threads must be specified as an argument for test purposes.
    This argument must be larger than 0, and is optional in real use (default = 10).
    """
    # Enforce thread_num argument for testing purposes.
    if len(sys.argv) != 2:
        print(f'Usage: python {sys.argv[0]} <thread_num>')
        sys.exit(1)
    # Define arguments.
    items = {
        'a': 1,
        'b': 2
    }
    # Define iterators.
    iterators = [1, 2, 3, 4, 5]
    # Execute function.
    results = threads(
        test_function,
        iterators,
        items,
        thread_num=int(sys.argv[1])
    )
    # Print results.
    print(results)
