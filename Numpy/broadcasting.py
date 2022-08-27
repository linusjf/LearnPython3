#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from numpy import array

a = np.arange(0,40,10)
print(a)
a = np.tile(a, (3, 1))
print(a)
a = a.T
print(a)
b = np.array([0, 1, 2])
print(a + b)
a = np.ones((4, 5))
# we assign an array of dimension 0 to an array of dimension 1
a[0] = 2
print(a)
a = np.arange(0, 40, 10)
print(a.shape)
# adds a new axis -> 2D array
a = a[:, np.newaxis] 
print(a.shape)
print(a)
print(a + b)

# define array
a = array([1, 2, 3])
print(a)
# define scalar
b = 2
print(b)
# broadcast
c = a + b
print(c)

# define array
A = array([
[1, 2, 3],
[1, 2, 3]])
print(A)
# define scalar
b = 2
print(b)
# broadcast
C = A + b
print(C)

# define two-dimensional array
A = array([
[1, 2, 3],
[1, 2, 3]])
print(A)
# define one-dimensional array
b = array([1, 2, 3])
print(b)
# broadcast
C = A + b
print(C)

# broadcasting error
# define two-dimensional array
A = array([
[1, 2, 3],
[1, 2, 3]])
print(A.shape)
# define one-dimensional array
b = array([1, 2])
print(b.shape)
try:
    # attempt broadcast
    C = A + b
    print(C)
except ValueError as ve:
    print("Value Error: {}".format(ve))
