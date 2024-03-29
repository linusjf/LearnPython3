#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

a = np.arange(1, 16, dtype=int).reshape(3, 5).T
print(a)
b = a[1:4:2]
print(b)
a = a.T
b = a[:, 1:4:2]
print(b)
a = np.arange(25).reshape(5, 5)
b = np.array([1.0, 5, 10, 15, 20])
print(a, b)
c = a / b[:, np.newaxis]
print(c)

a = np.random.rand(10, 3)
print(a)
b = np.where(a - 0.5 > 0, a - 0.5, 0.5 - a)
c = np.argmin(b, axis=1)
a = a[np.arange(0, 10), c]
print(a)
