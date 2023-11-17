#!/usr/bin/env python
"""
Futuregetresult.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : futuregetresult
# @created     : Friday Nov 17, 2023 18:12:54 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# get the result from a completed future task
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
    result = future.result()
    print(f'Got Result: {result}')
