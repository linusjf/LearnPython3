#!/usr/bin/env python
"""
Threadevent.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : threadevent
# @created     : Wednesday Nov 15, 2023 11:11:58 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of using an event object
from time import sleep
from secrets import randbelow
from threading import Thread
from threading import Event


def task(_event, _i, number):
    """# target task function"""
    # wait for the event to be set
    if not _event.wait(timeout=number):
        # begin processing
        value = randbelow(5)
        sleep(value)
        print(f'Thread {_i} got {value}')


# create a shared event object
event = Event()
# create a suite of threads
for i in range(5):
    thread = Thread(target=task, args=(event, i, randbelow(i + 1)))
    thread.start()
# block for a moment
print('Main thread blocking...')
sleep(2)
# start processing in all threads
event.set()
# wait for all the threads to finish...
