#!/usr/bin/env python
"""
Parentprocess.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : parentprocess
# @created     : Monday Nov 20, 2023 14:18:09 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""

# example of getting the parent process of a child process
from multiprocessing import parent_process
from multiprocessing import Process


def task():
    """function to execute in a new process"""
    # get the the parent process
    _process = parent_process()
    # report details
    print(_process)


# entry point
if __name__ == "__main__":
    # create a new process
    process = Process(target=task)
    # start the new process
    process.start()
    # wait for the new process to terminate
    process.join()
