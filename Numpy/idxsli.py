#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

a = np.arange(10)
print(a)
print(a[0], a[2], a[-1])
print(a[::-1])
a = np.diag(np.arange(3))
print(a)
print(a[1,1])
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
a = np.linspace(0,50,dtype=int,endpoint=False)
print(a)
b = a[0::2]
print(b)
b = a[50:0:-2]
print(b)
