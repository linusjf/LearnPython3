#!/usr/bin/env python
"""
Childprocesses.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : childprocesses
# @created     : Monday Nov 20, 2023 13:29:04 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# list all active child processes
from time import sleep
from multiprocessing import active_children
from multiprocessing import Process


def task():
    """function to execute in a new process"""
    # block for a moment
    sleep(1)


# entry point
if __name__ == "__main__":
    # create a number of child processes
    processes = [Process(target=task) for _ in range(5)]
    # start the child processes
    for process in processes:
        process.start()
    # get a list of all active child processes
    children = active_children()
    # report a count of active children
    print(f"Active Children Count: {len(children)}")
    # report each in turn
    for child in children:
        print(child)
