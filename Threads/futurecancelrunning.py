#!/usr/bin/env python
"""
Futurecancelrunning.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : futurecancelrunning
# @created     : Friday Nov 17, 2023 20:36:38 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of trying to cancel a running task via its future
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import wait


def work(sleep_time):
    """mock task that will sleep for a moment"""
    sleep(sleep_time)


# create a thread pool
with ThreadPoolExecutor(1) as executor:
    # start a long running task
    future = executor.submit(work, 2)
    running = future.running()
    print(f'Task running={running}')
    # try to cancel the task
    WAS_CANCELLED = future.cancel()
    print(f'Task was cancelled: {WAS_CANCELLED}')
    # wait for the task to finish
    wait([future])
    # check if it was cancelled
    running = future.running()
    cancelled = future.cancelled()
    done = future.done()
    print(f'Task running={running}, cancelled={cancelled}, done={done}')
