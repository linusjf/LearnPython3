#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sympy
from numpy import exp
from numpy import zeros,log
from midpoint import midpoint
from midpoint_double import midpoint_double1
from midpoint_double import midpoint_double2
from midpoint_triple import midpoint_triple1
from midpoint_triple import midpoint_triple2

def test_midpoint_one_exact_result():
    """Compare one hand-computed result."""
    v = lambda t: 3*(t**2)*exp(t**3)
    n = 4
    computed = midpoint(v, 0, 1, n)
    expected = 1.61897513780838 
    error = abs(expected - computed)
    tol = 1E-14
    success = error < tol
    msg = "error=%g > tol=%g" % (error, tol)
    assert success, msg

def test_midpoint_linear():
    """Check that linear functions are integrated exactly."""
    f = lambda x: 6*x - 4
    # Anti-derivative
    F = lambda x: 3*x**2 - 4*x 
    a = 1.2; b = 4.4
    expected = F(b) - F(a)
    tol = 1E-14
    for n in 2, 20, 21:
        computed = midpoint(f, a, b, n)
        error = abs(expected - computed)
        success = error < tol
        msg = 'n=%d, err=%g' % (n, error)
        assert success, msg

def convergence_rates(f, F, a, b, num_experiments=14):
    expected = F(b) - F(a)
    n = zeros(num_experiments, dtype=int)
    E = zeros(num_experiments)
    r = zeros(num_experiments-1)
    for i in range(num_experiments):
        n[i] = 2**(i+1)
        computed = midpoint(f, a, b, n[i])
        E[i] = abs(expected - computed)
        if i > 0:
            r_im1 = log(E[i]/E[i-1])/log(float(n[i])/n[i-1])
            r[i-1] = float('%.2f' % r_im1) # Truncate to two decimals
    return r

def test_midpoint_conv_rate():
    """Check empirical convergence rates against the expected -2."""
    v = lambda t: 3*(t**2)*exp(t**3)
    V = lambda t: exp(t**3)
    a = 1.1; b = 1.9
    r = convergence_rates(v, V, a, b, 14)
    print(r)
    tol = 0.01
    # show last 4 estimated rates
    msg = str(r[-4:])
    assert (abs(r[-1]) - 2) < tol, msg


def test_midpoint_double():
    def f(x, y):
        return 2*x + y

    nx = ny = 5
    expected = 9.0
    val = midpoint_double1(f, 0, 2, 2, 3, nx, ny)
    error = expected - val
    msg = 'nx=%d, ny=%d err=%g' % (nx,ny, error)
    tol = 1E-14
    assert error < tol , msg

def test_midpoint_double2():
    def f(x, y):
        return 2*x + y

    nx = ny = 5
    expected = 9.0
    val = midpoint_double2(f, 0, 2, 2, 3, nx, ny)
    error = expected - val
    msg = 'nx=%d, ny=%d err=%g' % (nx,ny, error)
    tol = 1E-14
    assert error < tol , msg

def test_midpoint_double_sympy():
    """Test that a linear function is integrated exactly."""
    def f(x, y):
        return 2*x + y

    a = 0;  b = 2;  c = 2;  d = 3
    x, y = sympy.symbols('x  y')
    I_expected = sympy.integrate(f(x, y), (x, a, b), (y, c, d))
    # Test three cases: nx < ny, nx = ny, nx > ny
    for nx, ny in (3, 5), (4, 4), (5, 3):
        I_computed1 = midpoint_double1(f, a, b, c, d, nx, ny)
        I_computed2 = midpoint_double2(f, a, b, c, d, nx, ny)
        tol = 1E-14
        #print I_expected, I_computed1, I_computed2
        assert abs(I_computed1 - I_expected) < tol
        assert abs(I_computed2 - I_expected) < tol

def test_midpoint_triple():
    """Test that a linear function is integrated exactly."""
    def g(x, y, z):
        return 2*x + y - 4*z

    a = 0;  b = 2;  c = 2;  d = 3;  e = -1;  f = 2
    x, y, z = sympy.symbols('x y z')
    I_expected = sympy.integrate(
        g(x, y, z), (x, a, b), (y, c, d), (z, e, f))
    for nx, ny, nz in (3, 5, 2), (4, 4, 4), (5, 3, 6):
        I_computed1 = midpoint_triple1(
            g, a, b, c, d, e, f, nx, ny, nz)
        I_computed2 = midpoint_triple2(
            g, a, b, c, d, e, f, nx, ny, nz)
        tol = 1E-14
        print(I_expected, I_computed1, I_computed2)
        assert abs(I_computed1 - I_expected) < tol
        assert abs(I_computed2 - I_expected) < tol

if __name__ == "__main__":
    test_midpoint_one_exact_result()
    test_midpoint_linear()
    test_midpoint_conv_rate()
    test_midpoint_double2()
    test_midpoint_double()
    test_midpoint_double_sympy()
    test_midpoint_triple()
