#!/usr/bin/env python
"""
Mainthreads.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : mainthreads
# @created     : Monday Nov 13, 2023 15:16:05 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of getting the current thread for the main thread
from threading import current_thread
from threading import main_thread
# get the main thread
thread = current_thread()
# report properties for the main thread
print(f'name={thread.name}, daemon={thread.daemon}, id={thread.ident}')
# example of getting the main thread
# get the main thread
thread = main_thread()
# report properties for the main thread
print(f'name={thread.name}, daemon={thread.daemon}, id={thread.ident}')
