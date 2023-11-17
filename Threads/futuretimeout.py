#!/usr/bin/env python
"""
Futuretimeout.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : futuretimeout
# @created     : Friday Nov 17, 2023 20:11:48 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# set a timeout when getting results from a future
from time import sleep
from concurrent.futures import ThreadPoolExecutor


def work():
    """mock task that will sleep for a moment"""
    sleep(1)
    return "all done"


# create a thread pool
with ThreadPoolExecutor() as executor:
    # start one thread
    future = executor.submit(work)
    # get the result from the task, wait for task to complete
    try:
        result = future.result(timeout=0.5)
        print(f'Got Result: {result}')
    except TimeoutError:
        print('Gave up waiting for a result')
