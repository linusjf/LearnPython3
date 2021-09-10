#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import exp

def trapezoidal(f, a, b, n):
    h = (b-a)/n
    fa = f(a)
    fb = f(b)
    result = 0.5*fa + 0.5*fb
    for i in range(1, n):
        val = a + i*h
        fval = f(val)
        result += fval
    result *= h
    return result

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
