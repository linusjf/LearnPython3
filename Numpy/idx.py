#!/usr/bin/env python
"""
Idx.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : idx
# @created     : Sunday Mar 19, 2023 14:10:27 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
import numpy as np

a = np.arange(10).reshape(2, 5)
print(a)
ixgrid = np.ix_([0, 1], [2, 4])
print(ixgrid)
print(ixgrid[0].shape, ixgrid[1].shape)
print(a[ixgrid])
ixgrid = np.ix_([True, True], [2, 4])
print(a[ixgrid])
ixgrid = np.ix_([True, True], [False, False, True, False, True])
print(a[ixgrid])
