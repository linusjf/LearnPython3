#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import exp
from numpy import log
from numpy import zeros
from trapezoidal import trapezoidal

def test_trapezoidal_one_exact_result():
    """Compare one hand-computed result."""
    v = lambda t: 3*(t**2)*exp(t**3)
    n = 2
    computed = trapezoidal(v, 0, 1, n)
    expected = 2.46364204124435
    error = abs(expected - computed)
    tol = 1E-14
    success = error < tol
    msg = "error=%g > tol=%g" % (error, tol)
    assert success, msg

def test_trapezoidal_linear():
    """Check that linear functions are integrated exactly."""
    f = lambda x: 6*x - 4
    # Anti-derivative
    F = lambda x: 3*x**2 - 4*x  
    a = 1.2; b = 4.4
    expected = 40.96
    tol = 1E-14
    for n in 2, 20, 21:
        computed = trapezoidal(f, a, b, n)
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
        computed = trapezoidal(f, a, b, n[i])
        E[i] = abs(expected - computed)
        if i > 0:
            r_im1 = log(E[i]/E[i-1])/log(float(n[i])/n[i-1])
            r[i-1] = float('%.2f' % r_im1) # Truncate to two decimals
    return r

def test_trapezoidal_conv_rate():
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

if __name__ == "__main__":
    test_trapezoidal_one_exact_result()
    test_trapezoidal_linear()
    test_trapezoidal_conv_rate()
