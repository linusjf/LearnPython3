#!/usr/bin/env python
"""
Matrices.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : matrices
# @created     : Sunday May 14, 2023 20:28:11 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
import sys
import numpy as np

print(f"Python version {sys.version}")
print(f"Numpy version: {np.__version__}")
# define a scalar
X = 6
print(X)
# define a vector
XV = np.array((1, 2, 3))
print(XV)
print(f"shape of vector: {XV.shape}")
print(f"size of vector: {XV.size}")
# defining a matrix
XM = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(XM)
print(f"shape of matrix: {XM.shape}")
print(f"size of matrix: {XM.size}")
