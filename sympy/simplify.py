#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sympy import *
x, y, z = symbols('x y z')
init_printing(use_unicode=True)
print(simplify(sin(x)**2 + cos(x)**2))

print(simplify((x**3 + x**2 - x - 1)/(x**2 + 2*x + 1)))
print(simplify(gamma(x)/gamma(x - 2)))
print(simplify(x**2 + 2*x + 1))

print(expand((x + 1)**2))
print(expand((x + 2)*(x - 3)))
print(expand((x + 1)*(x - 2) - (x - 1)*x))

print(factor(x**3 - x**2 + x - 1))
print(factor(x**2*z + 4*x*y*z + 4*y**2*z))
print(factor_list(x**2*z + 4*x*y*z + 4*y**2*z))

print(expand((cos(x) + sin(x))**2))
print(factor(cos(x)**2 + 2*cos(x)*sin(x) + sin(x)**2))

expr = x*y + x - 3 + 2*x**2 - z*x**2 + x**3
print(expr)
collected_expr = collect(expr, x)
print(collected_expr)

print(collected_expr.coeff(x, 2))

print(cancel((x**2 + 2*x + 1)/(x**2 + x)))
expr = 1/x + (3*x/2 - 2)/(x - 4)
print(expr)
print(cancel(expr))
expr = (x*y**2 - 2*x*y*z + x*z**2 + y**2 - 2*y*z + z**2)/(x**2 - 1)
print(expr)
print(cancel(expr))
print(factor(expr))
expr = (4*x**3 + 21*x**2 + 10*x + 12)/(x**4 + 5*x**3 + 5*x**2 + 4*x)
print(expr)
print(apart(expr))

print(acos(x))
print(cos(acos(x)))
print(asin(1))
print(trigsimp(sin(x)**2 + cos(x)**2))
print(trigsimp(sin(x)**4 - 2*cos(x)**2*sin(x)**2 + cos(x)**4))
print(trigsimp(sin(x)*tan(x)/sec(x)))
print(trigsimp(cosh(x)**2 + sinh(x)**2))
print(trigsimp(sinh(x)/tanh(x)))
print(expand_trig(sin(x + y)))
print(expand_trig(tan(2*x)))
print(trigsimp(sin(x)*cos(y) + sin(y)*cos(x)))

x, y = symbols('x y', positive=True)
a, b = symbols('a b', real=True)
z, t, c = symbols('z t c')
print(sqrt(x) == x**Rational(1, 2))
print(powsimp(x**a*x**b))
print(powsimp(x**a*y**a))
print(powsimp(t**c*z**c))
print(powsimp(t**c*z**c, force=True))
print((z*t)**2)
print(sqrt(x*y))
print(powsimp(z**2*t**2))
print(powsimp(sqrt(x)*sqrt(y)))

print(expand_power_exp(x**(a + b)))
print(expand_power_base((x*y)**a))
print(expand_power_base((z*t)**c))
print(expand_power_base((z*t)**c, force=True))
print(expand_power_exp(x**5))
print(powdenest((x**a)**b))
print(powdenest((z**a)**b))
