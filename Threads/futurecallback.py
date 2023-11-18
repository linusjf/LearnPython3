#!/usr/bin/env python
"""
Futurecallback.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : futurecallback
# @created     : Saturday Nov 18, 2023 09:17:02 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# add a callback option to a future object
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import wait


def custom_callback(_):
    """callback function to call when a task is completed"""
    print('Custom callback was called')


def work():
    """mock task that will sleep for a moment"""
    sleep(1)
    print('Task is done')


# create a thread pool
with ThreadPoolExecutor() as executor:
    # execute the task
    future = executor.submit(work)
    # add the custom callback
    future.add_done_callback(custom_callback)
    # wait for the task to complete
    wait([future])
