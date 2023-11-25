#!/usr/bin/env python
"""
Poolresults.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : poolresults
# @created     : Saturday Nov 25, 2023 13:00:57 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of getting a result from an asynchronous task issued with map_async
from time import sleep
from secrets import randbelow
from multiprocessing.pool import ThreadPool


def task(arg):
    """task executed in a thread worker"""
    # generate a random value between 0 and 1
    value = randbelow(100) / 100.0
    # block for a moment
    sleep(value)
    # return the generated value combined with the argument
    return arg + value


# protect the entry point
if __name__ == '__main__':
    # create the thread pool
    with ThreadPool() as pool:
        # issue tasks asynchronously
        async_result = pool.map_async(task, range(5))
        # wait for the task to complete and get the iterable of return values
        print('Waiting for results...')
        results = async_result.get()
        # iterate return values and report
        for result in results:
            # report the result
            print(f'Got: {result}')
