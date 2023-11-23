#!/usr/bin/env python
"""
Pausethread.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : pausethread
# @created     : Thursday Nov 23, 2023 19:07:45 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of pausing and resuming tasks in the threadpoolexecutor
from concurrent.futures import ThreadPoolExecutor
from threading import Event
from time import sleep


def task(_event):
    """task executed in the thread pool"""
    # main loop of the task
    for i in range(10):
        # check if the task is paused
        if not _event.is_set():
            # report a message
            print('Task is PAUSED')
            # wait for the event to be set
            _event.wait()
        # report a message
        print(f'Task is running [{i}]...')
        # do work
        sleep(0.5)


# protect the entry point
if __name__ == '__main__':
    # create the shared event
    event = Event()
    # set the event, allowing tasks to run freely
    event.set()
    # create the thread pool
    with ThreadPoolExecutor() as tpe:
        # issue the task
        _ = tpe.submit(task, event)
        # wait a moment
        sleep(2)
        # pause all tasks
        print('Main Pausing Tasks')
        event.clear()
        # wait a moment
        sleep(2)
        # resume
        print('Main Resuming Tasks')
        event.set()
