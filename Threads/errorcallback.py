#!/usr/bin/env python
"""
Errorcallback.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : errorcallback
# @created     : Monday Nov 27, 2023 11:53:59 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of issuing a task with apply_async() to the thread pool with
# an error callback
from secrets import randbelow
from time import sleep
from multiprocessing.pool import ThreadPool


def custom_error_callback(error):
    """handle any errors in the task function"""
    print(f'Got an Error: {error}')


def task(i):
    """task executed in a worker thread"""
    # report a message
    print('Task executing')
    # block for a moment
    sleep(i)
    # raise an exception
    raise Exception('Something bad happened')
    # report a message
    print('Task done')  # pylint: disable=unreachable


# protect the entry point
if __name__ == '__main__':
    # create and configure the thread pool
    pool = ThreadPool()
    # issue tasks to the thread pool
    pool.apply_async(task, args=(randbelow(10)/10.0, ),
                      error_callback=custom_error_callback)
    # close the thread pool
    pool.close()
    # wait for all tasks to finish
    pool.join()
