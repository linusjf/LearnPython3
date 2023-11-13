#!/usr/bin/env python
"""
Threadattributes.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : threadattributes
# @created     : Monday Nov 13, 2023 12:29:58 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of assessing whether a running thread is alive
from time import sleep
from threading import Thread
# create the thread
thread = Thread(target=lambda: sleep(1))
# report the thread is alive
print(thread.is_alive())
# report the native thread identifier
print(thread.native_id)
# report the thread identifier
print(thread.ident)
# report the daemon attribute
print(thread.daemon)
# report the thread name
print(thread.name)
# start the thread
thread.start()
# report the thread is alive
print(thread.is_alive())
# report the native thread identifier
print(thread.native_id)
# report the thread identifier
print(thread.ident)
# wait for the thread to finish
thread.join()
# report the thread is alive
print(thread.is_alive())
