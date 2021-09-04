#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

print(np.array([1, 2, 3]) + 1.5)
a = np.array([1, 2, 3])
print(a.dtype)
# <-- float is truncated to integer
a[0] = 1.9 
print(a)
a = np.array([1.7, 1.2, 1.6])
# <-- truncates to integer
b = a.astype(int) 
print(b)
a = np.array([1.2, 1.5, 1.6, 2.5, 3.5, 4.5])
b = np.around(a)
# still floating-point
print(b) 
c = np.around(a).astype(int)
print(c)    
print(np.array([1], dtype=int).dtype)
print(np.iinfo(np.int32).max, 2**31 - 1)
print(np.iinfo(np.uint32).max, 2**32 - 1)

print(np.iinfo(np.int64).max, 2**63 - 1)
print(np.finfo(np.float32).eps)
print(np.finfo(np.float64).eps)
print(np.float32(1e-8) + np.float32(1) == 1)
print(np.float64(1e-8) + np.float64(1) == 1)
