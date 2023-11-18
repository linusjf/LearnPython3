#!/usr/bin/env python
"""
Raiseexception.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : raiseexception
# @created     : Saturday Nov 18, 2023 13:39:52 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of handling an exception raised within a task
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import InvalidStateError


def work():
    """mock task that will sleep for a moment"""
    sleep(1)
    raise InvalidStateError('Something bad happened!')


# create a thread pool
with ThreadPoolExecutor() as executor:
    # execute our task
    future = executor.submit(work)
    # get the result from the task
    try:
        result = future.result()
    except InvalidStateError:
        print('Unable to get the result')
