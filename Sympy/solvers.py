#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sympy import *

x, y, z = symbols("x y z")
init_printing(use_unicode=True)
print(Eq(x, y))

print(solveset(Eq(x**2, 1), x))
print(solveset(Eq(x**2 - 1, 0), x))
print(solveset(x**2 - 1, x))

print(solveset(x**2 - x, x))
print(solveset(x - x, x, domain=S.Reals))
print(solveset(sin(x) - 1, x, domain=S.Reals))
print(solveset(exp(x), x))
# No solution exists
print(solveset(cos(x) - x, x))
# Not able to find solution
print(linsolve([x + y + z - 1, x + y + 2 * z - 3], (x, y, z)))

print(linsolve(Matrix(([1, 1, 1, 1], [1, 1, 2, 3])), (x, y, z)))
M = Matrix(((1, 1, 1, 1), (1, 1, 2, 3)))
system = A, b = M[:, :-1], M[:, -1]
print(linsolve(system, x, y, z))
a, b, c, d = symbols("a, b, c, d", real=True)
print(nonlinsolve([a**2 + a, a - b], [a, b]))
print(nonlinsolve([x * y - 1, x - 2], x, y))
print(nonlinsolve([x**2 + 1, y**2 + 1], [x, y]))
system = [x**2 - 2 * y**2 - 2, x * y - 2]
vars = [x, y]
print(nonlinsolve(system, vars))
system = [exp(x) - sin(y), 1 / y - 3]
print(nonlinsolve(system, vars))
print(nonlinsolve([x * y, x * y - x], [x, y]))
system = [a**2 + a * c, a - b]
print(nonlinsolve(system, [a, b]))

print(solve([x**2 - y**2 / exp(x)], [x, y], dict=True))
print(solve([sin(x + y), cos(x - y)], [x, y]))
print(solveset(x**3 - 6 * x**2 + 9 * x, x))
print(roots(x**3 - 6 * x**2 + 9 * x, x))
print(solve(x * exp(x) - 1, x))
f, g = symbols("f g", cls=Function)
print(f(x).diff(x))
diffeq = Eq(f(x).diff(x, x) - 2 * f(x).diff(x) + f(x), sin(x))
print(diffeq)
print(dsolve(diffeq, f(x)))
print(dsolve(f(x).diff(x) * (1 - sin(f(x))) - 1, f(x)))
