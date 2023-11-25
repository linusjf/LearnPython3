#!/usr/bin/env python
"""
Asyncresult.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : asyncresult
# @created     : Saturday Nov 25, 2023 12:53:45 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of getting a result from an asynchronous task issued with apply_async
from time import sleep
from secrets import randbelow
from multiprocessing.pool import ThreadPool


def task():
    """task executed by thread worker"""
    # generate a random value between 0 and 1
    value = randbelow(100) / 100.0
    # block for a moment
    sleep(value)
    # return the generated value
    return value


# protect the entry point
if __name__ == '__main__':
    # create the thread pool
    with ThreadPool() as pool:
        # issue a task asynchronously
        async_result = pool.apply_async(task)
        # wait for the task to complete and get the return value
        print('Waiting for result...')
        result = async_result.get()
        # report the result
        print(f'Got: {result}')
