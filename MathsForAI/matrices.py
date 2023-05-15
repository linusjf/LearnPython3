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
# defining a matrix of given dimensions
XONES = np.ones((3, 3))
print(XONES)
print(f"shape of matrix: {XONES.shape}")
print(f"size of matrix: {XONES.size}")
XZEROS = np.zeros((5, 5))
print(XZEROS)
print(f"shape of matrix: {XZEROS.shape}")
print(f"size of matrix: {XZEROS.size}")
XTENSOR = np.ones((3, 3, 3))
print(XTENSOR)
print(f"shape of tensor: {XTENSOR.shape}")
print(f"size of tensor: {XTENSOR.size}")
XTENSORONES = np.ones((3, 3, 3, 3))
print(XTENSORONES)
print(f"shape of tensor: {XTENSORONES.shape}")
print(f"size of tensor: {XTENSORONES.size}")
# indices
A = np.ones((5, 5), dtype=int)
print(A)
# indexing starts at 0
A[0, 1] = 2
print(A)
A[:, 1] = 3
print(A)
A[:, :] = 5
print(A)
# for higher dimensions just add an ibdex
B = np.ones((5, 5, 5), dtype=int)
B[:, 0, 0] = 4
print(B)
# matrix operations
C = np.matrix([[1, 2], [3, 4]])
D = np.ones((2, 2), dtype=int)
print(C)
print(D)
# element wise addition
E = C + D
print(E)
# element wise substraction
F = C - D
print(F)
# matrix multiplication
G = C * D
print(G)
