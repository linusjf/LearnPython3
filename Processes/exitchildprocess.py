#!/usr/bin/env python
"""
Exitchildprocess.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : exitchildprocess
# @created     : Friday Nov 24, 2023 14:10:06 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of exiting a child process
from time import sleep
from multiprocessing import Process
import sys


def task():
    """task executed in a new process"""
    # report a message
    print('Child process running')
    # block for a moment
    sleep(2)
    # exit the child process
    print('Exiting...')
    sys.exit(1)
    # never gets here
    print('Never gets here...')


# entry point
if __name__ == '__main__':
    # create a child process
    child = Process(target=task)
    # start the child process
    child.start()
    # wait for the child process to exit
    child.join()
    # check status of the child process
    print(f'Alive: {child.is_alive()}')
    # check the exitcode
    print(f'Exitcode: {child.exitcode}')
