#!/usr/bin/env python
"""
Futurestatus.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : futurestatus
# @created     : Friday Nov 17, 2023 18:09:15 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# check the status of a Future object for task executed by a thread pool
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import wait


def work():
    """mock task that will sleep for a moment"""
    sleep(0.5)


# create a thread pool
with ThreadPoolExecutor() as executor:
    # start one thread
    future = executor.submit(work)
    # confirm that the task is running
    running = future.running()
    done = future.done()
    print(f'Future running={running}, done={done}')
    # wait for the task to complete
    wait([future])
    # confirm that the task is done
    running = future.running()
    done = future.done()
    print(f'Future running={running}, done={done}')
