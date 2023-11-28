#!/usr/bin/env python
"""
Handlesigterm.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : handlesigterm
# @created     : Tuesday Nov 28, 2023 20:16:34 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of terminating a child process, and handling the signal
from time import sleep
from multiprocessing import Process
from signal import signal
from signal import SIGTERM
import sys


def handler(_, __):
    """handle signal"""
    print('Child process cleaning up...')
    sleep(2)
    # kill the process
    sys.exit(0)


def task():
    """custom task function"""
    # handle sigterm
    signal(SIGTERM, handler)
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
