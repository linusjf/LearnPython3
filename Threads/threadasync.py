#!/usr/bin/env python
"""
Threadasync.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : threadasync
# @created     : Saturday Nov 25, 2023 07:42:35 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of a one-off asynchronous task with a thread pool
from time import sleep
from multiprocessing.pool import ThreadPool


def task():
    """function to execute in a new thread"""
    # report a message
    print('Hello from the task')
    # sleep a moment
    sleep(1)
    # report another message
    print('Task is all done')


# entry point
if __name__ == '__main__':
    # create the thread pool
    with ThreadPool() as pool:
        # issue the task asynchronously
        async_result = pool.apply_async(task)
        # do other things, like report a message
        print('Main is doing other things...')
        # wait for the task to complete
        async_result.wait()
