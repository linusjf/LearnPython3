#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sympy import *
x, y, z = symbols('x y z')
init_printing(use_unicode=True)
print(diff(cos(x), x))
print(diff(exp(x**2), x))
print(diff(x**4, x, x, x))
print(diff(x**4, x, 3))
expr = exp(x*y*z)
print(diff(expr, x, y, y, z, z, z, z))
print(diff(expr, x, y, 2, z, 4))
print(diff(expr, x, y, y, z, 4))
print(expr.diff(x, y, y, z, 4))

print(expr.diff(x, y, y, z, 4))
deriv = Derivative(expr, x, y, y, z, 4)
print(deriv)
print(deriv.doit())

m, n, a, b = symbols('m n a b')
expr = (a*x + b)**m
print(expr.diff((x, n)))

print(integrate(cos(x), x))
print(sin(x))
print(integrate(exp(-x), (x, 0, oo)))
print(integrate(exp(-x**2 - y**2), (x, -oo, oo), (y, -oo, oo)))
expr = integrate(x**x, x)
print(expr)
expr = Integral(log(x)**2, x)
print(expr)
print(expr.doit())

integ = Integral((x**4 + x**2*exp(x) - x**2 - 2*x*exp(x) - 2*x -
    exp(x))*exp(x)/((x - 1)**2*(x + 1)**2*(exp(x) + 1)), x)
print(integ)
print(integ.doit())
integ = Integral(sin(x**2), x)
print(integ)
print(integ.doit())
integ = Integral(x**y*exp(-x), (x, 0, oo))
print(integ)
print(integ.doit())
