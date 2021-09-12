#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import linspace, zeros, pi, sin, exp
from trapezoidal import trapezoidal
import matplotlib.pyplot as plt

def integrate_coeffs(f, N, M):
    b = zeros(N)
    left_end = -pi; right_end = pi
    for n in range(1, N+1):
        f_sin = lambda t: f(t)*sin(n*t)
        b[n-1] = (1/pi)*trapezoidal(f_sin, left_end, right_end, M)
    return b

def test_integrate_coeffs():
    """Check that sin(nt) are integrated exactly by trapezoidal"""
    def f(t):
        return 1
    tol = 1E-14
    N = 10
    M = 100
    b = integrate_coeffs(f, N, M)
    print(b)
    for i in range(0, 10):
        # Supposed to be zero
        err = abs(b[i]) 
        assert err < tol, 'n = %d, err = %g' % (n,err)

def plot_approx(f, N, M, filename):
    def S_N(b,t):
        sum = 0
        for i in range(len(b)):
            sum += b[i]*sin((i+1)*t)
        return sum
    left_end = -pi  
    right_end = pi
    time = linspace(-pi, pi, 100)
    y = f(time)
    b = integrate_coeffs(f, N, M)
    y_approx = S_N(b, time)

    plt.figure(); 
    plt.plot(time, y, 'k-', time, y_approx, 'k--')
    plt.xlabel('t');  
    plt.ylabel('f (solid) and S (dashed)')
    plt.savefig(filename)

def application():
    def f(t):
        return (1/pi)*t
    N = 3
    M = 100
    b = integrate_coeffs(f, N, M)
    print(b)
    for N in [3, 6, 12, 24]:
        plot_filename = 'S_whenNis' + str(N) + '.pdf'
        plot_approx(f, N, M, plot_filename)
    def g(t):
        return exp(-(t-pi))
    plot_filename = 'new_f_S_whenNis' + str(100) + '.pdf'
    plot_approx(g, 100, M, plot_filename)

if __name__ == '__main__':
    application()
    test_integrate_coeffs()
