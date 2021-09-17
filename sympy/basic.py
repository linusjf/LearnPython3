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

expr = sin(2*x) + cos(2*x)
print(expand_trig(expr))
print(expr.subs(sin(2*x), 2*sin(x)*cos(x)))

expr = cos(x)
print(expr.subs(x, 0))
print(expr)
print(x)
expr = x**3 + 4*x*y - z
print(expr.subs([(x, 2), (y, 4), (z, 0)]))
expr = x**4 - 4*x**3 + 4*x**2 - 2*x + 3
replacements = [(x**i, y**i) for i in range(5) if i % 2 == 0]
print(replacements)
print(expr.subs(replacements))
expr = x**4 - 4*x**3 + 4*x**2 - 2*x + 3*y**0
replacements = [(x**i, y**i) for i in range(5) if i % 2 == 0]
print(replacements)
print(expr.subs(replacements))
