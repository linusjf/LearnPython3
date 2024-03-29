#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sympy import *

x, y, z = symbols("x y z")
init_printing(use_unicode=True)
print(simplify(sin(x) ** 2 + cos(x) ** 2))

print(simplify((x**3 + x**2 - x - 1) / (x**2 + 2 * x + 1)))
print(simplify(gamma(x) / gamma(x - 2)))
print(simplify(x**2 + 2 * x + 1))

print(expand((x + 1) ** 2))
print(expand((x + 2) * (x - 3)))
print(expand((x + 1) * (x - 2) - (x - 1) * x))

print(factor(x**3 - x**2 + x - 1))
print(factor(x**2 * z + 4 * x * y * z + 4 * y**2 * z))
print(factor_list(x**2 * z + 4 * x * y * z + 4 * y**2 * z))

print(expand((cos(x) + sin(x)) ** 2))
print(factor(cos(x) ** 2 + 2 * cos(x) * sin(x) + sin(x) ** 2))

expr = x * y + x - 3 + 2 * x**2 - z * x**2 + x**3
print(expr)
collected_expr = collect(expr, x)
print(collected_expr)

print(collected_expr.coeff(x, 2))

print(cancel((x**2 + 2 * x + 1) / (x**2 + x)))
expr = 1 / x + (3 * x / 2 - 2) / (x - 4)
print(expr)
print(cancel(expr))
expr = (x * y**2 - 2 * x * y * z + x * z**2 + y**2 - 2 * y * z + z**2) / (x**2 - 1)
print(expr)
print(cancel(expr))
print(factor(expr))
expr = (4 * x**3 + 21 * x**2 + 10 * x + 12) / (x**4 + 5 * x**3 + 5 * x**2 + 4 * x)
print(expr)
print(apart(expr))

print(acos(x))
print(cos(acos(x)))
print(asin(1))
print(trigsimp(sin(x) ** 2 + cos(x) ** 2))
print(trigsimp(sin(x) ** 4 - 2 * cos(x) ** 2 * sin(x) ** 2 + cos(x) ** 4))
print(trigsimp(sin(x) * tan(x) / sec(x)))
print(trigsimp(cosh(x) ** 2 + sinh(x) ** 2))
print(trigsimp(sinh(x) / tanh(x)))
print(expand_trig(sin(x + y)))
print(expand_trig(tan(2 * x)))
print(trigsimp(sin(x) * cos(y) + sin(y) * cos(x)))

x, y = symbols("x y", positive=True)
a, b = symbols("a b", real=True)
z, t, c = symbols("z t c")
print(sqrt(x) == x ** Rational(1, 2))
print(powsimp(x**a * x**b))
print(powsimp(x**a * y**a))
print(powsimp(t**c * z**c))
print(powsimp(t**c * z**c, force=True))
print((z * t) ** 2)
print(sqrt(x * y))
print(powsimp(z**2 * t**2))
print(powsimp(sqrt(x) * sqrt(y)))

print(expand_power_exp(x ** (a + b)))
print(expand_power_base((x * y) ** a))
print(expand_power_base((z * t) ** c))
print(expand_power_base((z * t) ** c, force=True))
print(expand_power_exp(x**5))
print(powdenest((x**a) ** b))
print(powdenest((z**a) ** b))

x, y = symbols("x y", positive=True)
n = symbols("n", real=True)
print(expand_log(log(x * y)))
print(expand_log(log(x / y)))
print(expand_log(log(x**2)))
print(expand_log(log(x**n)))
print(expand_log(log(z * t)))

print(expand_log(log(z**2)))
print(expand_log(log(z**2), force=True))

print(logcombine(log(x) + log(y)))

print(logcombine(n * log(x)))
print(logcombine(n * log(z)))

print(logcombine(n * log(z), force=True))

x, y, z = symbols("x y z")
k, m, n = symbols("k m n")
print(factorial(n))

print(binomial(n, k))
print(gamma(z))

print(hyper([1, 2], [3], z))
print(tan(x).rewrite(sin))
print(factorial(x).rewrite(gamma))
print(expand_func(gamma(x + 3)))
print(hyperexpand(hyper([1, 1], [2], z)))
expr = meijerg([[1], [1]], [[1], []], -z)
print(expr)
print(hyperexpand(expr))
n, k = symbols("n k", integer=True)
print(combsimp(factorial(n) / factorial(n - 3)))
print(combsimp(binomial(n + 1, k + 1) / binomial(n, k)))
print(gammasimp(gamma(x) * gamma(1 - x)))


def list_to_frac(l):
    expr = Integer(0)
    for i in reversed(l[1:]):
        expr += i
        expr = 1 / expr
    return l[0] + expr


print(list_to_frac([x, y, z]))
print(list_to_frac([1, 2, 3, 4]))
syms = symbols("a0:5")
print(syms)
a0, a1, a2, a3, a4 = syms
frac = list_to_frac(syms)
print(frac)

frac = cancel(frac)
print(frac)
l = []
frac = apart(frac, a0)
print(frac)
l.append(a0)
frac = 1 / (frac - a0)
print(frac)
frac = apart(frac, a1)
print(frac)
l.append(a1)
frac = 1 / (frac - a1)
frac = apart(frac, a2)
l.append(a2)
frac = 1 / (frac - a2)
frac = apart(frac, a3)
print(frac)
l.append(a3)
frac = 1 / (frac - a3)
frac = apart(frac, a4)
print(frac)
l.append(a4)
print(list_to_frac(l))

import random

l = list(symbols("a0:5"))
random.shuffle(l)
orig_frac = frac = cancel(list_to_frac(l))
del l
