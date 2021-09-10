#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sympy
import numpy as np
from MC_double import MonteCarlo_double

def test_MonteCarlo_double_rectangle_area():
    """Check the area of a rectangle."""
    def g(x, y):
        return (1 if (0 <= x <= 2 and 3 <= y <= 4.5) else -1)

    x0 = 0;  x1 = 3;  y0 = 2;  y1 = 5  # embedded rectangle
    n = 1000
    np.random.seed(8)      # must fix the seed!
    I_expected = 3.121092  # computed with this seed
    I_computed = MonteCarlo_double(
        lambda x, y: 1, g, x0, x1, y0, y1, n)
    assert abs(I_expected - I_computed) < 1E-14

def test_MonteCarlo_double_circle_r():
    """Check the integral of r over a circle with radius 2."""
    def g(x, y):
        xc, yc = 0, 0  # center
        R = 2          # radius
        return  R**2 - ((x-xc)**2 + (y-yc)**2)

    # Exact: integral of r*r*dr over circle with radius R becomes
    # 2*pi*1/3*R**3
    r = sympy.symbols('r')
    I_exact = sympy.integrate(2*sympy.pi*r*r, (r, 0, 2))
    print('Exact integral:', I_exact.evalf())
    x0 = -2;  x1 = 2;  y0 = -2;  y1 = 2
    n = 1000
    np.random.seed(6)
    I_expected = 16.7970837117376384  # Computed with this seed
    I_computed = MonteCarlo_double(
        lambda x, y: np.sqrt(x**2 + y**2),
        g, x0, x1, y0, y1, n)
    print('MC approximation %d samples: %.16f' % (n**2, I_computed))
    assert abs(I_expected - I_computed) < 1E-15

def test_MonteCarlo_samples():
    def g(x, y):
        return (1 if (0 <= x <= 2 and 3 <= y <= 4.5) else -1)
     
    expected = 3.0
    tol = 0.2
    res = MonteCarlo_double(lambda x, y: 1, g, 0, 3, 2, 5, 100)
    assert abs(expected - res) < tol  
    res = MonteCarlo_double(lambda x, y: 1, g, 0, 3, 2, 5, 1000)
    assert abs(expected - res) < tol  
    res = MonteCarlo_double(lambda x, y: 1, g, 0, 3, 2, 5, 1000)
    assert abs(expected - res) < tol  
    res = MonteCarlo_double(lambda x, y: 1, g, 0, 3, 2, 5, 2000)
    assert abs(expected - res) < tol  
    res = MonteCarlo_double(lambda x, y: 1, g, 0, 3, 2, 5, 2000)
    assert abs(expected - res) < tol  
    res = MonteCarlo_double(lambda x, y: 1, g, 0, 3, 2, 5, 5000)
    assert abs(expected - res) < tol  

if __name__ == '__main__':
    test_MonteCarlo_double_rectangle_area()
    test_MonteCarlo_double_circle_r()
    test_MonteCarlo_samples()
