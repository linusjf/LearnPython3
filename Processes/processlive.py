#!/usr/bin/env python
"""
Processlive.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : processlive
# @created     : Monday Nov 20, 2023 12:49:16 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of assessing whether a process is alive
from multiprocessing import Process

# entry point
if __name__ == "__main__":
    # create the process
    process = Process()
    # report the process is alive
    print(process.is_alive())
