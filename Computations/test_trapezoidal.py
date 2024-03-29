#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sympy
from numpy import exp
from numpy import log
from numpy import zeros
from trapezoidal import trapezoidal
from trapezoidal import trapezoidal_double


def test_trapezoidal():
    def f(x):
        return 2 * x**3

    a = 1
    b = 3
    n = 2
    numerical = trapezoidal(f, a, b, n)
    hand = 44.0
    error = abs(numerical - hand)
    tol = 1e-14
    assert error < tol, error


def test_trapezoidal_one_exact_result():
    """Compare one hand-computed result."""
    v = lambda t: 3 * (t**2) * exp(t**3)
    n = 2
    computed = trapezoidal(v, 0, 1, n)
    expected = 2.46364204124435
    error = abs(expected - computed)
    tol = 1e-14
    success = error < tol
    msg = "error=%g > tol=%g" % (error, tol)
    assert success, msg


def test_trapezoidal_linear():
    """Check that linear functions are integrated exactly."""
    f = lambda x: 6 * x - 4
    # Anti-derivative
    F = lambda x: 3 * x**2 - 4 * x
    a = 1.2
    b = 4.4
    expected = 40.96
    tol = 1e-14
    for n in 2, 20, 21:
        computed = trapezoidal(f, a, b, n)
        error = abs(expected - computed)
        success = error < tol
        msg = "n=%d, err=%g" % (n, error)
        assert success, msg


def convergence_rates(f, F, a, b, num_experiments=14):
    expected = F(b) - F(a)
    n = zeros(num_experiments, dtype=int)
    E = zeros(num_experiments)
    r = zeros(num_experiments - 1)
    for i in range(num_experiments):
        n[i] = 2 ** (i + 1)
        computed = trapezoidal(f, a, b, n[i])
        E[i] = abs(expected - computed)
        if i > 0:
            r_im1 = log(E[i] / E[i - 1]) / log(float(n[i]) / n[i - 1])
            r[i - 1] = float("%.2f" % r_im1)  # Truncate to two decimals
    return r


def test_trapezoidal_conv_rate():
    """Check empirical convergence rates against the expected -2."""
    v = lambda t: 3 * (t**2) * exp(t**3)
    V = lambda t: exp(t**3)
    a = 1.1
    b = 1.9
    r = convergence_rates(v, V, a, b, 14)
    print(r)
    tol = 0.01
    # show last 4 estimated rates
    msg = str(r[-4:])
    assert (abs(r[-1]) - 2) < tol, msg


def test_trapezoidal_double():
    """Test that a linear function is integrated exactly."""

    def f(x, y):
        return 2 * x + y

    a = 0
    b = 2
    c = 2
    d = 3
    x, y = sympy.symbols("x  y")
    I_expected = sympy.integrate(f(x, y), (x, a, b), (y, c, d))
    # Test three cases: nx < ny, nx = ny, nx > ny
    for nx, ny in (3, 5), (4, 4), (5, 3):
        I_computed = trapezoidal_double(f, a, b, c, d, nx, ny)
        tol = 1e-14
        # print I_expected, I_computed
        assert abs(I_computed - I_expected) < tol


if __name__ == "__main__":
    test_trapezoidal()
    test_trapezoidal_one_exact_result()
    test_trapezoidal_linear()
    test_trapezoidal_conv_rate()
    test_trapezoidal_double()
