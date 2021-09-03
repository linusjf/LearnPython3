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

b[0, 0] = 99
print(a)
a = np.zeros((3, 2))
b = a.T.reshape(3*2)
b[0] = 9
print(a)
z = np.array([1, 2, 3])
print(z)
z[:, np.newaxis]
z[np.newaxis, :]
a = np.arange(4*3*2).reshape(4, 3, 2)
print(a.shape)
print(a[0, 2, 1])
b = a.transpose(1, 2, 0)
print(b.shape)
print(b[2, 1, 0])
b[2, 1, 0] = -1
print(a[0, 2, 1])

a = np.arange(4)
a.resize((8,))
print(a)
b = a
try:
    print(a.resize((4,)))
except ValueError as ve:
    print(ve)
a.resize((4,),refcheck=False)
print(a)
