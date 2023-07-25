#!/usr/bin/env python
# -*- coding: utf-8 -*-

# importing the scipy and numpy packages
from scipy import linalg
import numpy as np
from numpy.linalg import LinAlgError

# Declaring the numpy arrays
a = np.array([[3, 2, 0], [1, -1, 0], [0, 5, 1]])
b = np.array([2, 4, -1])

# Passing the values to the solve function
x = linalg.solve(a, b)

# printing the result array
print(x)

# Declaring the numpy array
A = np.array([[1, 2], [3, 4]])

# Passing the values to the det function
x = linalg.det(A)

# printing the result
print(x)

# Declaring the numpy array
A = np.array([[1, 2], [3, 4]])

# Passing the values to the eig function
l, v = linalg.eig(A)

# printing the result for eigen values
print(l)

# printing the result for eigen vectors
print(v)

# Declaring the numpy array
a = np.random.randn(3, 2) + 1.0j * np.random.randn(3, 2)

# Passing the values to the eig function
U, s, Vh = linalg.svd(a)

# printing the result
print(U, Vh, s)

arr = np.array([[1, 2], [3, 4]])
print(linalg.det(arr))

arr = np.array([[3, 2], [6, 4]])
print(linalg.det(arr))

arr = np.array([[1, 2], [3, 4]])
iarr = linalg.inv(arr)
print(iarr)

np.allclose(np.dot(arr, iarr), np.eye(2))

arr = np.array([[3, 2], [6, 4]])
try:
    print(linalg.inv(arr))
except LinAlgError as lae:
    print(f"Error: {lae}")

arr = np.arange(9).reshape((3, 3)) + np.diag([1, 0, 1])
uarr, spec, vharr = linalg.svd(arr)
print(spec)
sarr = np.diag(spec)
svd_mat = uarr.dot(sarr).dot(vharr)
print(np.allclose(svd_mat, arr))
