#!/usr/bin/env python
"""
Catchexception.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : catchexception
# @created     : Saturday Nov 18, 2023 13:34:03 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of handling an exception raise within a task
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import InvalidStateError


def work():
    """mock task that will sleep for a moment"""
    sleep(1)
    try:
        raise InvalidStateError('Something bad happened!')
    except InvalidStateError:
        return 'Unable to get the result'


# create a thread pool
with ThreadPoolExecutor() as executor:
    # execute our task
    future = executor.submit(work)
    # get the result from the task
    result = future.result()
    print(result)
