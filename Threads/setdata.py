#!/usr/bin/env python
"""
Setdata.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : setdata
# @created     : Thursday Nov 16, 2023 15:16:51 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of a race condition with timing
from time import sleep
from threading import Thread
from threading import Condition
from threading import Event
from secrets import randbelow


def task(_condition, _event):
    """# thread waiting to be notified"""
    # insert a delay
    sleep(0.5)
    # wait to be notified
    with _condition:
        # indicate we are ready to be notified
        print('Thread: Ready')
        _event.set()
        # wait to be notified
        print('Thread: Waiting to be notified...')
        _condition.wait()
        print(VALUE)
    print('Thread: Notified')


VALUE = -1
# create the shared condition
condition = Condition()
# create the shared event
event = Event()
# create the new thread
thread = Thread(target=task, args=(condition, event))
# start the new thread
thread.start()
# busy wait for the new thread to get ready
print('Main: Waiting for threads to get ready...')
while not event.is_set():
    sleep(0.1)
# notify the new thread
print('Main: Notifying the thread')
with condition:
    VALUE = randbelow(10)
    condition.notify()
print('Main: Done')
