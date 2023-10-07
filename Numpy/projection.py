#!/usr/bin/env python
"""
Projection.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : projection
# @created     : Saturday Oct 07, 2023 14:07:47 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
import numpy as np
from numpy import linalg as lng
a = np.array([10, 20, 30, 40, 50])
b = np.array([60, 70, 80, 90, 100])
print(lng.norm(a))
vector_projection = (np.dot(a, b)/np.dot(b, b)) * b
print(vector_projection)
