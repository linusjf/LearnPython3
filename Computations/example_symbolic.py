#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sympy import cos, sin, diff, integrate, simplify, limit, solve, Symbol

x = Symbol("x")
y = Symbol("y")

# Algebraic computation
print(2 * x + 3 * x - y)
# Differentiates x**2 wrt. x
print(diff(x**2, x))
# differentiates cos(x) and sin(x) wrt. x
print(diff(cos(x), x))
print(diff(sin(x), x))
# Integrates cos(x) and sin(x) wrt. x
print(integrate(cos(x), x))
print(integrate(sin(x), x))
# Simplifies expression
print(simplify((x**2 + x**3) / x**2))
# Finds limit of sin(x)/x as x->0
print(limit(sin(x) / x, x, 0))
# Solves 5*x = 15
print(solve(5 * x - 15, x))
