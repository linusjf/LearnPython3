#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
For a straight line f(x) = ax + b, and the fixed point (2,f(2)) on
the line, the script tests whether (f(x_i) - f(2)) / (x_i - 2) = a
for randomly chosen x_i, i = 1,...,100.
"""

from random import random

def f(x):
    return a*x + b

a = 4.0; b = 1.0
c = 2; f_c = f(c)  # Fixed point on the line
epsilon = 1e-6
i = 0
for i in range(100):
    # random() returns number between 0 and 1
    x = 10*random() 
    numerator = f(x) - f_c
    denominator = x - c
    # To avoid zero division
    if denominator > epsilon:   
        fraction = numerator/denominator
        # The following printout should be very close to zero in
        # each case if the points are on the line
        print('For x = %g : %g' % (x,abs(fraction - a)))
