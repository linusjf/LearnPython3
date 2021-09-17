#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sympy import *
x, y, z = symbols("x y z")
expr = cos(x) + 1
print(expr.subs(x, y))
print(expr.subs(x, 0))
expr = x**y
print(expr)
expr = expr.subs(y, x**y)
print(expr)
expr = expr.subs(y, x**x)
print(expr)
