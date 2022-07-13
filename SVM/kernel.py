#!/usr/bin/env python
# -*- coding: utf-8 -*-
def polynomial_kernel(a, b):
    return a[0]**2 * b[0]**2 + 2*a[0]*b[0]*a[1]*b[1] + a[1]**2 * b[1]**2

x1 = [3,6]

# We do not transform the data.
x2 = [10,10] 

# 8100
print(polynomial_kernel(x1, x2)) 
