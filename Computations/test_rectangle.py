#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rectangle import rectangle

def test_rectangle_one_exact_result():
    """Compare one hand-computed result."""
    from math import exp
    v = lambda t: 3*(t**2)*exp(t**3)
    method = ['left', 'mid', 'right']
    n = 2
    exact = [0.4249306699000599, 1.3817914596908085, \
                                           4.5023534125886275]
    tol = 1E-14
    for i in range(len(method)):
        numerical = rectangle(v, 0, 1, n, method[i])
        err = abs(exact[i] - numerical)
        assert err < tol, err

def test_rectangle_linear():
    """Check that linear functions are integrated exactly
    (with midpoint) or with a known correctable error (left
    and right)"""
    method = ['left', 'mid', 'right']
    f = lambda x: 6*x - 4
    slope = 6
    F = lambda x: 3*x**2 - 4*x  # Anti-derivative
    # From the slope of f (i.e. 6), we know that left will
    # under-estimate the inegral by C (given below), while
    # right will over-estimate by C
    a = 1.2;  b = 4.4
    exact = F(b) - F(a)
    #tol = 1E-14
    tol = 1E-13        # Slightly relaxed compared to previously
    for n in 2, 20, 21:
        h = float(b-a)/n
        C = n*(0.5*slope*h**2)    # Correction term for left/right
        for i in range(len(method)):
            numerical = rectangle(f, a, b, n, method[i])
            if (method[i] == 'left'):
                numerical += C
            elif (method[i] == 'right'):
                numerical -= C
            err = abs(exact - numerical)
            assert err < tol, 'n = %d, err = %g' % (n,err)

def test_rectangle_conv_rate():
    """Check empirical convergence rates against the expected rate,
    which is -2 for midpoint and -1 for left and right."""
    from math import exp
    method = ['left', 'mid', 'right']
    v = lambda t: 3*(t**2)*exp(t**3)
    V = lambda t: exp(t**3)
    a = 1.1;  b = 1.9
    tol = 0.01
    for i in range(len(method)):
        r = convergence_rates(v, V, a, b, method[i], 14)
        print(r)
        if (method[i] == 'left') or (method[i] == 'right'):
            assert abs(abs(r[-1]) - 1) < tol, r[-4:]
        else:
            assert abs(abs(r[-1]) - 2) < tol, r[-4:]

def convergence_rates(f, F, a, b, height, num_experiments=14):
    from math import log
    from numpy import zeros
    exact = F(b) - F(a)
    n = zeros(num_experiments, dtype=int)
    E = zeros(num_experiments)
    r = zeros(num_experiments-1)
    for i in range(num_experiments):
        n[i] = 2**(i+1)
        numerical = rectangle(f, a, b, n[i], height)
        E[i] = abs(exact - numerical)
        if i > 0:
            r_im1 = log(E[i]/E[i-1])/log(float(n[i])/n[i-1])
            r[i-1] = float('%.2f' % r_im1)  # Truncate to two decimals
    return r

test_rectangle_one_exact_result()
test_rectangle_linear()
test_rectangle_conv_rate()
