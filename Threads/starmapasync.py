#!/usr/bin/env python
"""
Starmapasync.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : starmapasync
# @created     : Saturday Nov 25, 2023 13:32:12 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of getting a result from an asynchronous task issued
# with starmap_async
from time import sleep
from secrets import randbelow
from multiprocessing.pool import ThreadPool


def task(arg1, arg2, arg3):
    """task executed in a thread worker"""
    # generate a random value between 0 and 1
    value = randbelow(100) / 100.0
    # block for a moment
    print(f'Task ({arg1}, {arg2}, {arg3}) executing with {value}')
    sleep(value)
    # return the generated value combined with the argument
    return arg1 + arg2 + arg3 + value


# protect the entry point
if __name__ == '__main__':
    # create the thread pool
    with ThreadPool() as pool:
        # prepare arguments
        args = [(i, i*2, i*3) for i in range(5)]
        # issue tasks asynchronously
        async_result = pool.starmap_async(task, args)
        # wait for the task to complete and get the iterable of return values
        print('Waiting for results...')
        results = async_result.get()
        # iterate return values and report
        for result in results:
            # report the result
            print(f'Got: {result}')
    with ThreadPool() as pool:
        # prepare arguments
        items1 = [(i, randbelow(5), randbelow(5)) for i in range(10)]
        # issues tasks to thread pool
        _ = pool.starmap_async(task, items1)
        # prepare arguments
        items2 = [(i, randbelow(5), randbelow(5)) for i in range(11, 20)]
        # issues tasks to thread pool
        _ = pool.starmap_async(task, items2)
        # close the thread pool
        pool.close()
        # wait for all tasks to complete and threads to close
        pool.join()
    # thread pool is closed automatically
