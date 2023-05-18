#!/usr/bin/env python
"""
Eigendecomposition.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : eigendecomposition
# @created     : Thursday May 18, 2023 08:42:28 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
import sys
import numpy as np
from numpy import linalg

print(f"Python version {sys.version}")
print(f"Numpy version: {np.__version__}")


# define an array
A = np.arange(9) - 3
print(A)
B = A.reshape((3, 3))
print(B)
# Euclidean L2 norm -- default
print(linalg.norm(A))
print(linalg.norm(B))
# Frogenius norm is the L2 norm for a matrix
print(linalg.norm(B, "fro"))
# max norm P = infinity
print(linalg.norm(A, np.inf))
print(linalg.norm(B, np.inf))
# L1 norm
print(linalg.norm(A, 1))
print(linalg.norm(B, 1))
# vector normalization - normalization to produce a unit vector
norm = linalg.norm(A)
A_unit = A / norm
print(A_unit)
# the magnitude of unit vector is 1
print(linalg.norm(A_unit))

# find the eigen values and eigen vectors for a simple square matrix
C = np.diag(np.arange(1, 4))
print(C)
eigenvalues, eigenvectors = linalg.eig(C)
print(eigenvalues, eigenvectors)
# the eigen value w[i] corresponds to the eigen vector v[:, i]
for i in range(3):
    print(f"Eigen value: {eigenvalues[i]}")
    print(f"Eigen vector: {eigenvectors[:, i]}")
