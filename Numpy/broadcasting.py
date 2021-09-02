#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

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
