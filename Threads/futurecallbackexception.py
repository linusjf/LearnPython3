#!/usr/bin/env python
"""
Futurecallbackexception.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : futurecallbackexception
# @created     : Saturday Nov 18, 2023 12:01:06 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of handling an exception raised within a task
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import wait
from concurrent.futures import InvalidStateError


def custom_callback(_):
    """callback function to call when a task is completed"""
    print('Custom callback was called')


def work():
    """mock task that will sleep for a moment"""
    sleep(1)
    raise InvalidStateError('This is Fake!')
    return "never gets here"  # pylint: disable=unreachable


# create a thread pool
with ThreadPoolExecutor() as executor:
    # execute our task
    future = executor.submit(work)
    # add the custom callback
    future.add_done_callback(custom_callback)
    # wait for the task to complete
    wait([future])
    # check the status of the task after it has completed
    running = future.running()
    cancelled = future.cancelled()
    done = future.done()
    print(f'Task running={running}, cancelled={cancelled}, done={done}')
    # get the exception
    exception = future.exception()
    print(f'Exception={exception}')
    # get the result from the task
    try:
        result = future.result()
    except InvalidStateError:
        print('Unable to get the result')
