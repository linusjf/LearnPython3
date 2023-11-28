#!/usr/bin/env python
"""
Killprocess.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : killprocess
# @created     : Tuesday Nov 28, 2023 20:11:45 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of terminating a process
from time import sleep
from multiprocessing import Process


def task():
    """custom task function"""
    # execute a task in a loop
    while True:
        # block for a moment
        sleep(1)
        # report a message
        print('Worker process running...', flush=True)


# entry point
if __name__ == '__main__':
    # create a process
    process = Process(target=task)
    # run the process
    process.start()
    # wait for a moment
    sleep(5)
    # terminate the process
    process.terminate()
    # continue on...
    print('Parent is continuing on...')
    # create a process
    process = Process(target=task)
    # run the process
    process.start()
    # wait for a moment
    sleep(5)
    # kill the process
    process.kill()
    # continue on...
    print('Parent is continuing on...')
