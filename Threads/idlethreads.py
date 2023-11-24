#!/usr/bin/env python
"""
Idlethreads.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : idlethreads
# @created     : Friday Nov 24, 2023 10:51:20 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of idle threads not being released after tasks are done
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import wait
from time import sleep
import threading


def task():
    """task executed in the thread pool"""
    # block for a moment
    sleep(1)


# create the thread pool
with ThreadPoolExecutor(4) as tpe:
    # issue four tasks
    futures = [tpe.submit(task) for _ in range(4)]
    # wait for the tasks to complete
    _ = wait(futures)
    # wait a while for any idle threads to be released
    print('Main thread waiting for a minute...')
    sleep(60)
    # report all running threads
    print('Running threads:')
    for thread in threading.enumerate():
        print(f'\t{thread}')
