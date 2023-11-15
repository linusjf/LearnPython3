#!/usr/bin/env python
"""
Deadlock.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : deadlock
# @created     : Wednesday Nov 15, 2023 18:44:29 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of a deadlock caused by a thread waiting on itself
from threading import Thread
from threading import Lock


def task(_lock):
    """# task to be executed in a new thread"""
    print('Thread acquiring lock...')
    with _lock:
        print('Thread acquiring lock again...')
        with _lock:
            # will never get here
            pass


# create the mutex lock
lock = Lock()
# create and configure the new thread
thread = Thread(target=task, args=(lock,))
# start the new thread
thread.start()
# wait for threads to exit...
thread.join()
