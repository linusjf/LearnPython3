#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sympy import *

x, y, z = symbols("x y z")
init_printing(use_unicode=True)
print(diff(cos(x), x))
print(diff(exp(x**2), x))
print(diff(x**4, x, x, x))
print(diff(x**4, x, 3))
expr = exp(x * y * z)
print(diff(expr, x, y, y, z, z, z, z))
print(diff(expr, x, y, 2, z, 4))
print(diff(expr, x, y, y, z, 4))
print(expr.diff(x, y, y, z, 4))

print(expr.diff(x, y, y, z, 4))
deriv = Derivative(expr, x, y, y, z, 4)
print(deriv)
print(deriv.doit())

m, n, a, b = symbols("m n a b")
expr = (a * x + b) ** m
print(expr.diff((x, n)))

print(integrate(cos(x), x))
print(sin(x))
print(integrate(exp(-x), (x, 0, oo)))
print(integrate(exp(-(x**2) - y**2), (x, -oo, oo), (y, -oo, oo)))
expr = integrate(x**x, x)
print(expr)
expr = Integral(log(x) ** 2, x)
print(expr)
print(expr.doit())

integ = Integral(
    (x**4 + x**2 * exp(x) - x**2 - 2 * x * exp(x) - 2 * x - exp(x))
    * exp(x)
    / ((x - 1) ** 2 * (x + 1) ** 2 * (exp(x) + 1)),
    x,
)
print(integ)
print(integ.doit())
integ = Integral(sin(x**2), x)
print(integ)
print(integ.doit())
integ = Integral(x**y * exp(-x), (x, 0, oo))
print(integ)
print(integ.doit())


print(limit(sin(x) / x, x, 0))

expr = x**2 / exp(x)
print(expr.subs(x, oo))
print(limit(expr, x, oo))

expr = Limit((cos(x) - 1) / x, x, 0)
print(expr)
print(expr.doit())
print(limit(1 / x, x, 0, "+"))
print(limit(1 / x, x, 0, "-"))

expr = exp(sin(x))
print(expr.series(x, 0, 4))
print(x + x**3 + x**6 + O(x**4))
print(x * O(1))
print(expr.series(x, 0, 4).removeO())
print(exp(x - 6).series(x, x0=6))

f, g = symbols("f g", cls=Function)
print(differentiate_finite(f(x) * g(x)))

f = Function("f")
dfdx = f(x).diff(x)
print(dfdx.as_finite_difference())

f = Function("f")
d2fdx2 = f(x).diff(x, 2)
h = Symbol("h")
print(d2fdx2.as_finite_difference([-3 * h, -h, 2 * h]))
print(finite_diff_weights(2, [-3, -1, 2], 0)[-1][-1])

x_list = [-3, 1, 2]
y_list = symbols("a b c")
print(apply_finite_diff(1, x_list, y_list, 0))
