#!/usr/bin/env python
"""
Localthreadstate.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : localthreadstate
# @created     : Saturday Nov 18, 2023 19:32:37 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of thread local storage for worker threads
from time import sleep
from secrets import randbelow
import threading
from concurrent.futures import ThreadPoolExecutor


def initializer_worker(_local):
    """function for initializing the worker thread"""
    # generate a unique value for the worker thread
    _local.key = randbelow(10) / 10.0
    # store the unique worker key in a thread local variable
    print(f'Initializing worker thread {_local.key}')


def task(_local):
    """a mock task that sleeps
    for a random amount of time less than one second"""
    # access the unique key for the worker thread
    mykey = _local.key
    # make use of it
    sleep(mykey)
    return f'Worker using {mykey}'


# get the local context
local = threading.local()
# create a thread pool
executor = ThreadPoolExecutor(max_workers=2,
                              initializer=initializer_worker,
                              initargs=(local,))
# dispatch asks
futures = [executor.submit(task, local) for _ in range(10)]
# wait for all threads to complete
for future in futures:
    result = future.result()
    print(result)
# shutdown the thread pool
executor.shutdown()
print('done')
