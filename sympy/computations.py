#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sympy import *
x, t, z, nu = symbols('x t z nu')
init_printing(use_unicode=True)
print(diff(sin(x)*exp(x), x))
print(integrate(exp(x)*sin(x) + exp(x)*cos(x), x))
print(integrate(sin(x**2), (x, -oo, oo)))
print(limit(sin(x)/x, x, 0))
print(solve(x**2 - 2, x))
y = Function('y')
print(dsolve(Eq(y(t).diff(t, t) - y(t), exp(t)), y(t)))
print(Matrix([[1, 2], [2, 2]]).eigenvals())
print(besselj(nu, z).rewrite(jn))
print(latex(Integral(cos(x)**2, (x, 0, pi))))
