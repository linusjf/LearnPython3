#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.ravel())
print(a.T)
print(a.T.ravel())
print(a.shape)
b = a.ravel()
b = b.reshape((2, 3))
print(b)
# unspecified (-1) value is inferred
print(a.reshape((2, -1))) 
