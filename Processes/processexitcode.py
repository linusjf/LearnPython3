#!/usr/bin/env python
"""
Processexitcode.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : processexitcode
# @created     : Monday Nov 20, 2023 13:19:21 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of checking the exit status of a child process
from time import sleep
from multiprocessing import Process


def task():
    """function to execute in a new process"""
    sleep(1)


# entry point
if __name__ == '__main__':
    # create the process
    process = Process(target=task)
    # report the exit status
    print(process.exitcode)
    # start the process
    process.start()
    # report the exit status
    print(process.exitcode)
    # wait for the process to finish
    process.join()
    # report the exit status
    print(process.exitcode)
