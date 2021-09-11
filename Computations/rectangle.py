#!/usr/bin/env python
# -*- coding: utf-8 -*-

def rectangle(f, a, b, n, height='left'):
    """Uses a rectangle method for integrating f. The height of
    each rectangle is computed either at the left end, middle or
    right end of each sub-interval"""
    h = float(b-a)/n
    if height == 'left':
        start = a
    elif height == 'mid':
        start = a + h/2.0
    else:      # Must be right end
        start = a + h
    result = 0
    for i in range(n):
        result += f((start) + i*h)
    result *= h
    return result

