#!/usr/bin/env python
"""
Contextswitch.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : contextswitch
# @created     : Thursday Nov 16, 2023 16:29:35 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of changing the context switch interval
from sys import getswitchinterval
from sys import setswitchinterval
# report the interval
interval = getswitchinterval()
print(f'Context switch interval: {interval} seconds')
# decrease the interval
setswitchinterval(1.0)
# report the new interval
interval = getswitchinterval()
print(f'Context switch interval: {interval} seconds')
