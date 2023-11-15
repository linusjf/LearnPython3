#!/usr/bin/env python
"""
Jointhread.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : jointhread
# @created     : Thursday Nov 16, 2023 04:41:49 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of joining a thread
from time import sleep
from threading import Thread


def task():
    """# target function"""
    # block for a moment
    sleep(1)
    # report a message
    print('All done in the new thread')


# create a new thread
thread = Thread(target=task)
# start the new thread
thread.start()
# wait for the new thread to finish
print('Main: Waiting for thread to terminate...')
thread.join()
# continue on
print('Main: Continuing on')
