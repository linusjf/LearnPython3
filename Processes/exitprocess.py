#!/usr/bin/env python
"""
Exitprocess.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : exitprocess
# @created     : Friday Nov 24, 2023 14:08:27 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of exiting the main process
from time import sleep
import sys
# report a message
print('Main process running')
# block for a moment
sleep(2)
# exit the main process
print('Exiting...')
sys.exit(0)
# never gets here
print('Never gets here...')
