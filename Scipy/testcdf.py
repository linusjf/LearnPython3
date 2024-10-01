#!/usr/bin/env python
"""
Testcdf.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : testcdf
# @created     : Monday Sep 30, 2024 18:44:28 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
from scipy import stats

val = stats.f.cdf(0.5, 3, 397)
print(val)
val = stats.f.sf(0.5, 3, 397)
print(val)
val = stats.f.sf(0.5, 1, 396)
print(val)
val = stats.f.sf(0.1, 1, 396)
print(val)
