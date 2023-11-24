#!/usr/bin/env python
"""
Exitparentprocess.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : exitparentprocess
# @created     : Friday Nov 24, 2023 14:15:01 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of exiting the main process while child is running
from time import sleep
from multiprocessing import Process
from multiprocessing import parent_process
import sys


def task():
    """function executed in a new process"""
    # report a message
    print('Child process running', flush=True)
    # wait a moment
    sleep(2)
    # check the status of the parent process
    parent = parent_process()
    print(f'Alive: {parent.is_alive()}', flush=True)
    print(f'Exitcode: {parent.exitcode}')


# entry point
if __name__ == '__main__':
    # create a new process
    child = Process(target=task)
    # start the new process
    child.start()
    # block for a moment
    sleep(1)
    # exit the main process
    print('Exiting...')
    sys.exit()
    # never gets here
    print('Never gets here...')
