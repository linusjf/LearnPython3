#!/usr/bin/env python
"""
Processname.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : processname
# @created     : Monday Nov 20, 2023 12:43:54 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of accessing the child process name
from multiprocessing import Process
# entry point
if __name__ == '__main__':
    # create the process
    process = Process()
    # report the process name
    print(process.name)
