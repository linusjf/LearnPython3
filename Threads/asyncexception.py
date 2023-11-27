#!/usr/bin/env python
"""
Asyncexception.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : asyncexception
# @created     : Monday Nov 27, 2023 12:13:44 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of issuing a task with apply_async() to the thread pool and
# handle exception
from time import sleep
from multiprocessing.pool import ThreadPool
from multiprocessing import ProcessError


def task():
    """task executed in a worker thread"""
    # report a message
    print('Task executing')
    # block for a moment
    sleep(1)
    # raise an exception
    raise Exception('Something bad happened')
    # report a message
    print('Task done')  # pylint: disable=unreachable
    # return a value
    return "DONE!"


# protect the entry point
if __name__ == '__main__':
    # create and configure the thread pool
    pool = ThreadPool()
    # issue tasks to the thread pool
    result = pool.apply_async(task)
    # wait for the return value
    try:
        value = result.get()
    except ProcessError as e:
        print(f'Failed with: {e}')
    # close the thread pool
    pool.close()
