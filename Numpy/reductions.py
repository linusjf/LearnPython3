#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

x = np.array([1, 2, 3, 4])
print(np.sum(x))
print(x.sum())
x = np.array([[1, 1], [2, 2]])
print(x)
# columns (first dimension)
print(x.sum(axis=0))
print(x[:, 0].sum(), x[:, 1].sum())
# rows (second dimension)
print(x.sum(axis=1))
print(x[0, :].sum(), x[1, :].sum())
x = np.random.rand(2, 2, 2)
print(x.sum(axis=2)[0, 1])
print(x[0, 1, :].sum())
x = np.array([1, 3, 2])
print(x.min())
print(x.max())

# index of minimum
print(x.argmin())
# index of maximum
print(x.argmax())
print(np.all([True, True, False]))
print(np.any([True, True, False]))
a = np.zeros((100, 100))
print(np.any(a != 0))
print(np.all(a == a))
a = np.array([1, 2, 3, 2])
b = np.array([2, 2, 3, 2])
c = np.array([6, 4, 4, 5])
print(((a <= b) & (b <= c)).all())
x = np.array([1, 2, 3, 1])
y = np.array([[1, 2, 3], [5, 6, 1]])
print(x.mean())
print(np.median(x))
# last axis
print(np.median(y, axis=-1))
# full population standard dev.
print(x.std())
print(x.prod())
print(x.cumsum())
