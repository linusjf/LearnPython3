#!/usr/bin/env python
"""
Wait.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : wait
# @created     : Tuesday Nov 28, 2023 20:07:16 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of joining a process that is not running
from time import sleep
from multiprocessing import Process


def task():
    """target function"""
    # block for a moment
    sleep(1)
    # report a message
    print('All done in the new process')


# entry point
if __name__ == '__main__':
    # create a new process
    process = Process(target=task)
    # start the new process
    process.start()
    # block for a moment
    print('Main: blocking for a moment...')
    sleep(2)
    # wait for the new process to finish
    print('Main: Waiting for process to terminate...')
    process.join()
    # continue on
    print('Main: Continuing on')
