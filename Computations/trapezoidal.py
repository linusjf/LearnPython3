#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import exp
from numpy import linspace

def trapezoidal(f, a, b, n):
    h = float(b-a)/n
    x = linspace(a, b, n+1)
    s = sum(f(x)) - 0.5*f(a) - 0.5*f(b)
    return h*s

def trapezoidal_double(f, a, b, c, d, nx, ny):
    hx = (b - a)/float(nx)
    hy = (d - c)/float(ny)
    I = 0.25*(f(a, c) + f(a, d) + f(b, c) + f(b, d))
    Ix = 0
    for i in range(1, nx):
        xi = a + i*hx
        Ix += f(xi, c) + f(xi, d)
    I += 0.5*Ix
    Iy = 0
    for j in range(1, ny):
        yj = c + j*hy
        Iy += f(a, yj) + f(b, yj)
    I += 0.5*Iy
    Ixy = 0
    for i in range(1, nx):
        for j in range(1, ny):
            xi = a + i*hx
            yj = c + j*hy
            Ixy += f(xi, yj)
    I += Ixy
    I *= hx*hy
    return I

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
