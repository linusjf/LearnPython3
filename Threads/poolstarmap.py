#!/usr/bin/env python
"""
Poolstarmap.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : poolstarmap
# @created     : Monday Nov 27, 2023 19:26:29 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of using starmap() with the thread pool
from secrets import randbelow
from time import sleep
from multiprocessing.pool import ThreadPool


def task(identifier, value):
    """task executed in a worker thread"""
    # report a message
    print(f'Task {identifier} executing with {value}')
    # block for a moment
    sleep(value)
    # return the generated value
    return (identifier, value)


# protect the entry point
if __name__ == '__main__':
    # create and configure the thread pool
    with ThreadPool() as pool:
        # prepare arguments
        items = [(i, randbelow(5)) for i in range(10)]
        # execute tasks and thread results in order
        for result in pool.starmap(task, items):
            print(f'Got result: {result}')
    # thread pool is closed automatically
    # create and configure the thread pool
    with ThreadPool() as pool:
        # prepare arguments
        items = [(i, randbelow(5)) for i in range(10)]
        # issue tasks to the thread pool and wait for tasks to complete
        pool.starmap(task, items)
    # thread pool is closed automatically
    # create and configure the thread pool
    with ThreadPool() as pool:
        # prepare arguments
        items = [(i, randbelow(5)) for i in range(10)]
        # execute tasks and thread results in order
        for result in pool.starmap(task, items, chunksize=2):
            print(f'Got result: {result}')
    # thread pool is closed automatically
