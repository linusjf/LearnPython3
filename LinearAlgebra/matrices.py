#!/usr/bin/env python
"""
Matrices.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : matrices
# @created     : Wednesday Oct 18, 2023 15:15:59 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
import numpy as np
import pandas as pd
import seaborn as sns
A = np.array([[0, 2],  # 1st row
              [1, 4]])  # 2nd row
print(f'a 2x2 Matrix:\n{A}')
A = np.array([[0, 2],
              [1, 4]])
B = np.array([[3, 1],
              [-3, 2]])
print(A + B)
np.add(A, B)
ALPHA = 2
A = np.array([[1, 2],
              [3, 4]])
print(ALPHA * A)
print(np.multiply(ALPHA, A))
A = np.array([[0, 2],
              [1, 4]])
x = np.array([[1],
              [2]])
print(A @ x)
print(np.dot(A, x))
B = np.array([[1, 3],
              [2, 1]])
print(A @ B)
print(np.dot(A, B))
