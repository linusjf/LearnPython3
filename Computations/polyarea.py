#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Computes the area of a polygon from vertex
coordinates only.
"""

def polyarea(x, y):
    n = len(x)
    # next we may initialize area with those terms in the
    # sum that does not follow the "increasing index pattern"
    area = x[n-1]*y[0] - y[n-1]*x[0]
    for i in range(0,n-1,1):
        area += x[i]*y[i+1] - y[i]*x[i+1]
    return 0.5*abs(area)

# pentagon
x = [0, 2, 2, 1, 0]
y = [0, 0, 2, 3, 2]
print('Area pentagon (true value = 5): ', polyarea(x, y))
# quadrilateral
x = [0, 2, 2, 0]
y = [0, 0, 2, 2]
print('Area quadrilateral (true value = 4): ', polyarea(x, y))
# triangle
x = [0, 2, 0]
y = [0, 0, 2]
print('Area triangle (true value = 2): ', polyarea(x, y))
