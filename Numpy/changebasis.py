#!/usr/bin/env python
"""
Changebasis.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : changebasis
# @created     : Tuesday Oct 10, 2023 13:49:47 IST
# @description : https://www.kaggle.com/code/dhgupta/change-of-basis/notebook
# -*- coding: utf-8 -*-'
######################################################################
"""
import numpy as np

# Case 1: Moving from standard basis to non-standard
# vector v1 in standard basis coordinates
v1 = np.array([[4], [9]])
# standard basis
B1 = np.array([[1, 0], [0, 1]])
# alternate basis
B2 = np.array([[1, 1], [2, 3]])
v2 = np.array([[3], [1]])
# create the transformation matrix
B2inv = np.linalg.inv(B2)
print(B2inv)
M = np.dot(B2inv, B1)
print(M)
print(np.dot(M, B2))

# perform change of basis
v2calc = np.dot(M, v1)
print(v2)
print(v2calc)
print(np.dot(B1, v1))
print(np.dot(B2, v2))

# Case 2: Moving from non-standard basis to standard

# alternate basis
B1 = np.array([[1, 1], [2, 3]])
v1 = np.array([[3], [1]])
# vector v2 in standard basis coordinates
v2 = np.array([[4], [9]])
# standard basis
B2 = np.array([[1, 0], [0, 1]])

# create the transformation matrix
B2inv = np.linalg.inv(B2)
print(B2inv)
M = np.dot(B2inv, B1)
print(M)
print(np.dot(M, B2))

# perform change of basis
v2calc = np.dot(M, v1)
print(v2)
print(v2calc)
print(np.dot(B1, v1))
print(np.dot(B2, v2))
