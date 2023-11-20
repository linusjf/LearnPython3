#!/usr/bin/env python
"""
Cpucount.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : cpucount
# @created     : Monday Nov 20, 2023 13:33:27 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of reporting the number of logical cpu cores
from multiprocessing import cpu_count
# get the number of cpu cores
num_cores = cpu_count()
# report details
print(num_cores)
