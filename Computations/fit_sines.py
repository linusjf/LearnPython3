#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import zeros, linspace, sin, sqrt, pi, copy, arange
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('fit_sines.pdf')
print("Setup Complete")

def sinesum(t, b):
    """
    Computes S as the sum over n of b_n * sin(n*t).
    For each point in time (M) we loop over all b_n to
    produce one element S[M], i.e. one element in
    S corresponds to one point in time.
    """
    S = zeros(len(t))
    for M in range(0, len(t), 1):
        for n in range(1, len(b)+1, 1):
            S[M] += b[n-1]*sin(n*t[M])
    return S

def test_sinesum():
    t = zeros(2); t[0] = -pi/2;  t[1] = pi/4
    b = zeros(2); b[0] = 4.0;  b[1] = -3
    print(sinesum(t, b))

def plot_compare(f, N, M):
    time = linspace(left_end, right_end, M)
    y = f(time)
    S = sinesum(time, b)
    plt.plot(time, y, 'b-', time, S, 'r--')
    plt.xlabel('Time')
    plt.ylabel('f (blue) and S (red)')
    plt.show()
    pp.savefig()
    plt.clf()

def error(b, f, M):
    time = linspace(left_end, right_end, M)
    y = f(time)
    S = sinesum(time, b)
    E = 0
    for i in range(len(time)):
        E += sqrt((y[i] - S[i])**2)
    return E

def trial(f, N):
    M = 500
    new_trial = True
    while new_trial:
        for i in range(N):
            text = 'Give b' + str(i+1) + ' : '
            b[i] = input(text)
        plot_compare(f, N, M)
        print('The error is: ', error(b, f, M))
        answer = raw_input('Another trial (y/n)? ')
        if answer == 'n':
            new_trial = False

def f(t):
    return (1/pi)*t

def automatic_fit(f, N):
    """Search for b-values, - just pick limits and step"""
    global b
    M = 500
    # Produce and store an initially "smallest" error
    b[0] = -1; b[1] = -1; b[2] = -1
    test_b = copy(b)
    smallest_E = error(test_b, f, M)
    db = 0.1
    for b1 in arange(-1, 1+db, db):
        for b2 in arange(-1, 1+db, db):
            for b3 in arange(-1, 1+db, db):
                test_b[0] = b1; test_b[1] = b2;
                test_b[2] = b3
                E = error(test_b, f, M)
                if E < smallest_E:
                    b = copy(test_b)
                    smallest_E = E
    plot_compare(f, N, M)
    print('The b coeffiecients: ', b)
    print('The smallest error found: ', smallest_E)

left_end = -pi;  right_end = pi
N = 3
b = zeros(N)
#test_sinesum()
#trial(f, N)
automatic_fit(f, N)
pp.close()
