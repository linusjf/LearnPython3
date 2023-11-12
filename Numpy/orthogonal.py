#!/usr/bin/env python
"""
Orthogonal.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : orthogonal
# @created     : Tuesday Oct 10, 2023 21:24:17 IST
# @description : http://surl.li/lzwxw
# https://datascienceparichay.com/article/numpy-check-if-a-matrix-is-orthogonal/
# -*- coding: utf-8 -*-'
######################################################################
"""
import numpy as np

# create matrices
ar1 = np.array([
    [0, 1, 0],
    [-1, 0, 0],
    [0, 0, 1]
])

ar2 = np.array([
    [1, 2, 3],
    [0, 0, 2],
    [4, 5, 6]
])

# dot product of matrix and its transpose
dot_product = np.dot(ar1, ar1.T)

# create an identity matrix of the same shape as ar1
identity_matrix = np.identity(len(ar1))

# check if matrix is orthogonal
print(np.allclose(dot_product, identity_matrix))

# dot product of matrix and its transpose
dot_product = np.dot(ar2, ar2.T)

# create an identity matrix of the same shape as ar2
identity_matrix = np.identity(len(ar2))

# check if matrix is orthogonal
print(np.allclose(dot_product, identity_matrix))

# check if matrix is orthogonal
print(np.allclose(ar1.T, np.linalg.inv(ar1)))

# check if matrix is orthogonal
print(np.allclose(ar2.T, np.linalg.inv(ar2)))
