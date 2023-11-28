#!/usr/bin/env python
"""
Restartprocess.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : restartprocess
# @created     : Tuesday Nov 28, 2023 19:43:32 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of restarting a process
from time import sleep
from multiprocessing import Process


def task():
    """custom target function"""
    # block for a moment
    sleep(1)
    # report a message
    print('Hello from the new process')


# entry point
if __name__ == '__main__':
    # create a new process
    process = Process(target=task)
    # start the process
    process.start()
    # wait for the process to finish
    process.join()
    # create a new process with the same config
    process2 = Process(target=task)
    # start the new process
    process2.start()
    # wait for the new process to finish
    process2.join()
