#!/usr/bin/env python
"""
Stopthread.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : stopthread
# @created     : Wednesday Nov 15, 2023 22:43:02 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of stopping a new thread
from time import sleep
from threading import Thread
from threading import Event
from secrets import randbelow


def task(_event):
    """# custom task function"""
    # execute a task in a loop
    for i in range(5):
        # block for a moment
        sleep(randbelow(5))
        # check for stop
        if _event.is_set():
            break
        # report a message
        print(f'{i}: Worker thread running...')
    print('Worker closing down')


# create the event
event = Event()
# create and configure a new thread
thread = Thread(target=task, args=(event,))
# start the new thread
thread.start()
# block for a while
sleep(randbelow(25))
# stop the worker thread
print('Main stopping thread')
event.set()
# wait for the new thread to finish
thread.join()
