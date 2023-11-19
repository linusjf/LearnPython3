#!/usr/bin/env python
"""
Process.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : process
# @created     : Sunday Nov 19, 2023 16:10:21 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of running a function in a new process
from multiprocessing import Process


def task():
    """a task to execute in another process"""
    print('This is another process', flush=True)


# entry point for the program
if __name__ == '__main__':
    # define a task to run in a new process
    p = Process(target=task)
    # start the task in a new process
    p.start()
    # wait for the task to complete
    p.join()
