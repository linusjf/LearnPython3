#!/usr/bin/env python
"""
Processpid.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : processpid
# @created     : Monday Nov 20, 2023 12:47:33 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of reporting the native process identifier
from multiprocessing import Process
# entry point
if __name__ == '__main__':
    # create the process
    process = Process()
    # report the process identifier
    print(process.pid)
    # start the process
    process.start()
    # report the process identifier
    print(process.pid)
