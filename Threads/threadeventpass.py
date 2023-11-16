#!/usr/bin/env python
"""
Threadeventpass.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : threadeventpass
# @created     : Thursday Nov 16, 2023 14:56:58 IST
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


def task(_event, _i):
    """# target task function"""
    # begin processing
    value = randbelow(5)
    sleep(value)
    print(f'Thread {_i} got {value}')
    global VALUE  # pylint: disable=global-statement
    VALUE = value
    _event.set()


VALUE = -1
# create a shared event object
event = Event()
# create a suite of threads
thread = Thread(target=task, args=(event, 0))
thread.start()
# block for a moment
print('Main thread blocking...')
sleep(2)
# start processing in all threads
# wait for the event to be set
event.wait()
print(VALUE)
