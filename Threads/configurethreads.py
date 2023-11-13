#!/usr/bin/env python
"""
Configurethreads.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : configurethreads
# @created     : Monday Nov 13, 2023 13:45:10 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of setting the thread name in the constructor
from threading import Thread
# create a thread with a custom name
thread = Thread(name='MyThread')
# report thread name
print(thread.name)
thread.name = "NewNameThread"
# report thread name
print(thread.name)

# create a daemon thread
thread = Thread(daemon=True)
# report if the thread is a daemon
print(thread.daemon)
thread.daemon = False
# report if the thread is a daemon
print(thread.daemon)
