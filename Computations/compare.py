#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sympy as sp
from numpy import exp
from trapezoidal import trapezoidal
from midpoint import midpoint
from simpsons import simpson
from gaussian import gauss
from scipy.integrate import fixed_quad

def f(y):
    return exp(-y**2)

a = 0
b = 2
print('    n        midpoint          trapezoidal          simpson          gaussian')
for i in range(1, 16):
    n = 2**i
    m = midpoint(f, a, b, n)
    t = trapezoidal(f, a, b, n)
    s = simpson(f, a, b, n)
    #g = gauss(f, a, b, n)
    g = fixed_quad(f,a,b,n=n)[0]
    print('%7d %.16f %.16f %.16f %.16f' % (n, m, t, s, g))

def g(x):
    return x*(x-1)

a = 2;  b = 6;
n = 100

numerical_trap = trapezoidal(g, a, b, n)
numerical_mid  = midpoint(g, a, b, n)

# Compute exact integral by sympy
x = sp.symbols('x')
F = sp.integrate(g(x))
exact = F.subs(x, b) - F.subs(x, a)
exact = exact.evalf()

error_trap = abs(numerical_trap - exact)
error_mid  = abs(numerical_mid - exact)

print('For n = %d, we get:' % (n))
print('Numerical trapezoid: %g , Error: %g' % \
                                 (numerical_trap,error_trap))
print('Numerical midpoint: %g , Error: %g' % \
                                 (numerical_mid,error_mid))
