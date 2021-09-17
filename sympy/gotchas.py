#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sympy import *

x = symbols('x')
print(x + 1)

x, y, z = symbols('x y z')
a, b = symbols('b a')
print(a,b)
print(b,a)
crazy = symbols('unrelated')
print(crazy + 1)
x = symbols('x')
expr = x + 1
x = 2
print(expr)

