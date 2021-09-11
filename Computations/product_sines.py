#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import pi,sin
from midpoint import midpoint

a = -pi
b = pi
n = 1000
exact = 0
tol = 1e-14

for i in range(1,11):
    for j in range(1,11):
        def f(x):
            return sin(i*x)*sin(j*x)
       
        if (i != j):
            I = midpoint(f,a,b,n)
            print(i,j,I)
            assert abs(I) < tol


