#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

a = np.array([2, 3, 4])
print(a)
print(a.dtype)
b = np.array([1.2, 3.5, 5.1])
print(b)
print(b.dtype)
# WRONG
# a = np.array(1,2,3,4)
# RIGHT
a = np.array([1, 2, 3, 4])
b = np.array([(1.5, 2, 3), (4, 5, 6)])
print(b)
c = np.array([[1, 2], [3, 4]], dtype=complex)
print(c)
print(np.zeros((3, 4)))
# dtype can also be specified
print(np.ones((2, 3, 4), dtype=np.int16))
# uninitialized
print(np.empty((2, 3)))

print(np.arange(10, 30, 5))
# it accepts float arguments
print(np.arange(0, 2, 0.3))

from numpy import pi

# 9 numbers from 0 to 2
np.linspace(0, 2, 9)
# useful to evaluate function at lots of points
x = np.linspace(0, 2 * pi, 100)
print(x.dtype)
f = np.sin(x)
print(f.dtype)
d = np.array([1 + 2j, 3 + 4j, 5 + 6 * 1j])
print(d.dtype)

# create array
from numpy import array

# create array
l = [1.0, 2.0, 3.0]
a = array(l)
# display array
print(a)
# display array shape
print(a.shape)
# display array data type
print(a.dtype)

# create empty array
from numpy import empty

a = empty([3, 3])
print(a)

# create zero array
from numpy import zeros

a = zeros([3, 5])
print(a)

# create one array
from numpy import ones

a = ones([5])
print(a)
