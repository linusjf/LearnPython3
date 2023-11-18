#!/usr/bin/env python
"""
Callbackexception.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : callbackexception
# @created     : Saturday Nov 18, 2023 14:50:59 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# add callbacks to a future, one of which raises an exception
from time import sleep
from concurrent.futures import ThreadPoolExecutor


def custom_callback1(_):
    """callback function to call when a task is completed"""
    raise Exception('Something bad happened!')
    # never gets here
    print('Callback 1 called.')  # pylint: disable=unreachable


def custom_callback2(_):
    """callback function to call when a task is completed"""
    print('Callback 2 called.')


def work():
    """mock task that will sleep for a moment"""
    sleep(1)
    return 'Task is done'


# create a thread pool
with ThreadPoolExecutor() as executor:
    # execute the task
    future = executor.submit(work)
    # add the custom callbacks
    future.add_done_callback(custom_callback1)
    future.add_done_callback(custom_callback2)
    # wait for the task to complete and get the result
    result = future.result()
    # wait for callbacks to finish
    sleep(0.1)
    print(result)
