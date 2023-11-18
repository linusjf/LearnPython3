#!/usr/bin/env python
"""
Explicitexceptioncheck.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : explicitexceptioncheck
# @created     : Saturday Nov 18, 2023 14:43:40 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of handling an exception raised within a task
from time import sleep
from concurrent.futures import ThreadPoolExecutor


def work():
    """mock task that will sleep for a moment"""
    sleep(1)
    raise Exception('Something bad happened!')


# create a thread pool
with ThreadPoolExecutor() as executor:
    # execute our task
    future = executor.submit(work)
    # get the result from the task
    exception = future.exception()
    # handle exceptional case
    if exception:
        print(exception)
    else:
        result = future.result()
        print(result)
