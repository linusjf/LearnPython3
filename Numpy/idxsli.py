#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

a = np.arange(10)
print(a)
print(a[0], a[2], a[-1])
print(a[::-1])
a = np.diag(np.arange(3))
print(a)
print(a[1, 1])
# third line, second column
a[2, 1] = 10
print(a)
print(a[1])
a = np.arange(10)
print(a)
# [start:end:step]
print(a[2:9:3])
print(a[:4])
print(a[1:3])
print(a[::2])
print(a[3:])
a = np.arange(10)
a[5:] = 10
print(a)
b = np.arange(5)
a[5:] = b[::-1]
print(a)
a = np.linspace(0, 50, dtype=int, endpoint=False)
print(a)
b = a[0::2]
print(b)
b = a[50:0:-2]
print(b)
print(np.arange(6))
print(np.arange(0, 51, 10))
print(np.arange(0, 51, 10)[:, np.newaxis])
# add 1D array to 2D array
a = np.arange(6) + np.arange(0, 51, 10)[:, np.newaxis]
print(a)
print(a[0, 3:5])
print(a[4:, 4:])
print(a[:, 2])
print(a[2::2, ::2])
a = np.ones((4, 4), dtype=np.int8)
a[2, 3] = 2
a[3, 1] = 6
print(a)
a = np.diag(np.arange(7))
a = a[1::, 2::]
print(a)
a = [[4, 3], [2, 1]]
a = np.tile(a, (2, 3))
print(a)
a = np.arange(10)
print(a)
b = a[::2]
print(b)
print(np.may_share_memory(a, b))
b[0] = 12
print(b)
# (!)
print(a)
a = np.arange(10)
# force a copy
c = a[::2].copy()
c[0] = 12
print(a)
print(np.may_share_memory(a, c))

np.random.seed(3)
a = np.random.randint(0, 21, 15)
print(a)
print((a % 3 == 0))
mask = a % 3 == 0
# or, a[a%3==0]
extract_from_a = a[mask]
# extract a sub-array with the mask
print(extract_from_a)
a[a % 3 == 0] = -1
print(a)
a = np.arange(0, 100, 10)
print(a)
# note: [2, 3, 2, 4, 2] is a Python list
a[[2, 3, 2, 4, 2]]
a[[9, 7]] = -100
print(a)

a = np.arange(10)
idx = np.array([[3, 4], [9, 7]])
print(idx.shape)
print(a[idx])

a = np.arange(6) + np.arange(0, 51, 10)[:, np.newaxis]
print(a)
print(a[(0, 1, 2, 3, 4), (1, 2, 3, 4, 5)])
print(a[3:, [0, 2, 5]])
mask = np.array([1, 0, 1, 0, 0, 1], dtype=bool)
print(a[mask, 2])
