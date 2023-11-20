#!/usr/bin/env python
"""
Processdaemon.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : processdaemon
# @created     : Monday Nov 20, 2023 12:46:06 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of assessing whether a process is a daemon
from multiprocessing import Process
# entry point
if __name__ == '__main__':
    # create the process
    process = Process()
    # report the daemon attribute
    print(process.daemon)
