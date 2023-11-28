#!/usr/bin/env python
"""
Jointimeout.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : jointimeout
# @created     : Tuesday Nov 28, 2023 20:04:42 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of joining a process with a timeout
from time import sleep
from multiprocessing import Process


def task():
    """target function"""
    # block for a moment
    sleep(5)
    # report a message
    print('All done in the new process')


# entry point
if __name__ == '__main__':
    # create a new process
    process = Process(target=task)
    # start the new process
    process.start()
    # wait for the new process to finish
    print('Main: Waiting for process to terminate...')
    process.join(timeout=2)
    # check if the process is still alive
    if process.is_alive():
        print('Main: The target process is still running')
    else:
        print('Main: The target process has terminated')
