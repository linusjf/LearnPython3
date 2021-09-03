#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

a = np.array([[4, 3, 5], [1, 2, 1]])
b = np.sort(a, axis=1)
print(b)
a.sort(axis=1)
print(a)
a = np.array([4, 3, 1, 2])
j = np.argsort(a)
print(j)
print(a[j])
a = np.array([4, 3, 1, 2])
j_max = np.argmax(a)
j_min = np.argmin(a)
print(j_max, j_min)
