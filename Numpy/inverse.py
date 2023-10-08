#!/usr/bin/env python
"""
Inverse.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : inverse
# @created     : Sunday Oct 08, 2023 13:23:56 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
import numpy as np
from numpy import linalg
A = np.array([[1, 2], [3, 4]])
print(A)
Ainv = linalg.inv(A)
print(Ainv)
b = np.array([5, 11])
print(b)
X = np.dot(Ainv, b)
print(X)
print(np.dot(A, X))
