#!/usr/bin/env python
# -*- coding: utf-8 -*-

from trapezoidal import trapezoidal

def test_trapezoidal_linear_scale():
    """Check that linear functions are integrated exactly"""
    f = lambda x: 6E8*x - 4E6
    F = lambda x: 3E8*x**2 - 4E6*x  # Anti-derivative
    #a = 1.2;  b = 4.4
    a = 1.2/6E8;  b = 4.4/6E8       # Scale interval down
    exact = F(b) - F(a)
    tol = 1E-14
    for n in 2, 20, 21:
        numerical = trapezoidal(f, a, b, n)
        err = abs(exact - numerical)
        msg = 'n = %d, err = %g' % (n, err)
        assert err < tol, msg
        print(msg)

def test_trapezoidal_linear_reldiff():
    """
    Check that linear functions are integrated exactly.
    Use relative and not absolute difference.
    """
    f = lambda x: 6E8*x - 4E6
    F = lambda x: 3E8*x**2 - 4E6*x  # Anti-derivative
    a = 1.2;  b = 4.4               # Scale interval down
    exact = F(b) - F(a)
    tol = 1E-14
    for n in 2, 20, 21:
        numerical = trapezoidal(f, a, b, n)
        err = abs(exact - numerical)/exact
        msg = 'n = %d, err = %g' % (n, err)
        assert err < tol, msg
        print(msg)

def test_trapezoidal_conv_rate():
    """Check empirical convergence rates against the expected -2."""
    #from math import exp
    f = lambda x: 6E8*x - 4E6
    F = lambda x: 3E8*x**2 - 4E6*x  # Anti-derivative
    a = 1.1;  b = 1.9
    r = convergence_rates(f, F, a, b, 14)
    print(r)
    tol = 0.01
    assert abs(abs(r[-1]) - 0) < tol, r[-4:]

def convergence_rates(f, F, a, b, num_experiments=14):
    from math import log
    from numpy import zeros
    exact = F(b) - F(a)
    n = zeros(num_experiments, dtype=int)
    E = zeros(num_experiments)
    r = zeros(num_experiments-1)
    for i in range(num_experiments):
        n[i] = 2**(i+1)
        numerical = trapezoidal(f, a, b, n[i])
        E[i] = abs(exact - numerical)
        print(E[i])
        if i > 0:
            r_im1 = log(E[i]/E[i-1])/log(float(n[i])/n[i-1])
            r[i-1] = float('%.2f' % r_im1)  # Truncate, two decimals
    return r

test_trapezoidal_linear_scale()
test_trapezoidal_linear_reldiff()
test_trapezoidal_conv_rate()
