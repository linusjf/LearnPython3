#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
a = np.array([1, 2, 3, 4])
b = np.array([4, 2, 2, 4])
print(a == b)
print(a > b)
a = np.array([1, 2, 3, 4])
b = np.array([4, 2, 2, 4])
c = np.array([1, 2, 3, 4])
np.array_equal(a, b)
np.array_equal(a, c)
a = np.array([1, 1, 0, 0], dtype=bool)
b = np.array([1, 0, 1, 0], dtype=bool)
print(np.logical_or(a, b))
print(np.logical_and(a, b))
a = np.arange(5)
print(np.sin(a))
print(np.log(a))
print(np.exp(a))
a = np.arange(4)
try:
    a + np.array([1, 2])
except ValueError as ve:
    print(ve)
# see help(np.triu)
a = np.triu(np.ones((3, 3)), 1)
print(a)
print(a.T)
a = np.arange(9).reshape(3, 3)
a.T[0, 2] = 999
print(a.T)
print(a)
print(np.allclose([1e10,1e-7], 
                  [1.00001e10,1e-8]))
print(np.allclose([1e10,1e-8], 
                  [1.00001e10,1e-9]))
print(np.allclose([1e10,1e-8],
                  [1.0001e10,1e-9]))
print(np.allclose([1.0, np.nan], 
                  [1.0, np.nan]))
print(np.allclose([1.0, np.nan], 
                  [1.0, np.nan], 
                  equal_nan=True))
