#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy 
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

str_expr = "x**2 + 3*x - 1/2"
expr = sympify(str_expr)
print(expr)
print(expr.subs(x, 2))
expr = sqrt(8)
print(expr.evalf())
print(pi.evalf(100))

expr = cos(2*x)
print(expr.evalf(subs={x: 2.4}))
one = cos(1)**2 + sin(1)**2
print((one - 1).evalf())
print((one - 1).evalf(chop=True))

a = numpy.arange(10) 
expr = sin(x)
f = lambdify(x, expr, "numpy") 
print(f(a))

f = lambdify(x, expr, "math")
print(f(0.1))

def mysin(x):
    """
    My sine. Note that this is only accurate for small x.
    """
    return x

f = lambdify(x, expr, {"sin":mysin})
print(f(0.1))
