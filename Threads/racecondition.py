#!/usr/bin/env python
"""
Racecondition.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : racecondition
# @created     : Wednesday Nov 15, 2023 15:55:49 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of a race condition with timing
from time import sleep
from threading import Thread
from threading import Condition


def task(_condition):
    """# thread waiting to be notified"""
    # insert a delay
    sleep(0.5)
    # wait to be notified
    print('Thread: Waiting to be notified...')
    with _condition:
        _condition.wait()
    print('Thread: Notified')


# create the shared condition
condition = Condition()
# create the new thread
thread = Thread(target=task, args=(condition,))
# start the new thread
thread.start()
# notify the new thread
print('Main: Notifying the thread')
with condition:
    condition.notify()
print('Main: Done')
