#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import exp
from numpy import linspace

def trapezoidal(f, a, b, n):
    h = float(b-a)/n
    x = linspace(a, b, n+1)
    s = sum(f(x)) - 0.5*f(a) - 0.5*f(b)
    return h*s

def application():
    v = lambda t: 3*(t**2)*exp(t**3)
    n = int(input('n: '))
    numerical = trapezoidal(v, 0, 1, n)
    print(numerical)

    # Compare with exact result
    V = lambda t: exp(t**3)
    exact = V(1) - V(0)
    print(exact)
    error = exact - numerical
    print('n=%d: exact=%.16f, calc=%.16f, error: %g' % (n, exact,numerical, error))

if __name__ == '__main__':
    application()
