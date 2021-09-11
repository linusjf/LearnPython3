#!/usr/bin/env python
# -*- coding: utf-8 -*-

from adaptive import adaptive_integration

def f(x):
    return x**x

eps = 1E-4
a = 0.0;  b = 2.0

# Choose midpoint method
n = adaptive_integration(f, a, b, eps, 'midpoint')
if n > 0:
    print('Sufficient n is: %d' % (n))
else:
    # The negative n is returned to signal that the upper limit of n
    # was passed
    print('No n was found in %d iterations' % (abs(n)))

print("---------------------------------------------------")
# Choose midpoint method
n = adaptive_integration(f, a, b, eps, 'trapezoidal')
if n > 0:
    print('Sufficient n is: %d' % (n))
else:
    # The negative n is returned to signal that the upper limit of n
    # was passed
    print('No n was found in %d iterations' % (abs(n)))
