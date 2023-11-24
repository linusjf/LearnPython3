#!/usr/bin/env python
"""
Noidlethreads.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : noidlethreads
# @created     : Friday Nov 24, 2023 08:45:44 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of no idle threads after threadpoolexecutor is created
from concurrent.futures import ThreadPoolExecutor
from time import sleep
import threading
# create a thread pool
tpe = ThreadPoolExecutor()
# wait a moment
sleep(1)
# report all running threads
for thread in threading.enumerate():
    print(thread)
# shutdown the thread pool
tpe.shutdown()
