#!/usr/bin/env python
"""
Reentrantlock.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : reentrantlock
# @created     : Tuesday Nov 14, 2023 14:00:45 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of a reentrant lock
from time import sleep
from secrets import randbelow
from threading import Thread
from threading import RLock


def report(_lock, identifier):
    """# reporting function"""
    # acquire the lock
    with _lock:
        print(f'>thread {identifier} done')


def task(_lock, identifier, value):
    """# work function"""
    # acquire the lock
    with _lock:
        print(f'>thread {identifier} sleeping for {value}')
        sleep(value)
        # report
        report(_lock, identifier)


# create a shared reentrant lock
lock = RLock()
# start a few threads that attempt to execute the same critical section
for i in range(10):
    # start a thread
    Thread(target=task, args=(lock, i, randbelow(10))).start()
# wait for all threads to finish...
