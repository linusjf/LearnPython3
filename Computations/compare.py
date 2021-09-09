#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
