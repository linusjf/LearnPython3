#!/usr/bin/env python
"""
Determinant.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : determinant
# @created     : Sunday Oct 08, 2023 21:11:39 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
import numpy as np
from numpy import linalg
A = np.array([[1, 2], [3, 4]])
print(linalg.det(A))
Ainv = linalg.inv(A)
print(Ainv)
B = np.array([[5, 11], [10, 22]])
print(B)
print(linalg.det(B))
print(linalg.inv(B))
