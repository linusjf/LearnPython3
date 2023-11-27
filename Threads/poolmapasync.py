#!/usr/bin/env python
"""
Poolmapasync.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : poolmapasync
# @created     : Monday Nov 27, 2023 15:03:20 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of parallel map_async() with the thread pool
from secrets import randbelow
from time import sleep
from multiprocessing.pool import ThreadPool


def task(identifier):
    """task executed in a worker thread"""
    # generate a value
    value = randbelow(100000) / 100000.0
    # report a message
    print(f'Task {identifier} executing with {value}')
    # block for a moment
    sleep(value)
    # return the generated value
    return value


# protect the entry point
if __name__ == '__main__':
    # create and configure the thread pool
    with ThreadPool() as pool:
        # issues tasks to thread pool
        result = pool.map_async(task, range(10))
        # iterate results
        for result in result.get():
            print(f'Got result: {result}')
    # thread pool is closed automatically
    with ThreadPool() as pool:
        # issues tasks to thread pool
        result = pool.map_async(task, range(10))
        # wait for tasks to complete
        result.wait()
    # thread pool is closed automatically
    with ThreadPool() as pool:
        # issues tasks to thread pool
        _ = pool.map_async(task, range(10))
        # issues tasks to thread pool
        _ = pool.map_async(task, range(10, 20))
        # close the thread pool
        pool.close()
        # wait for all tasks to complete and threads to close
        pool.join()
    # thread pool is closed automatically
