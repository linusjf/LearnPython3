#!/usr/bin/env python
# -*- coding: utf-8 -*-
from numpy import exp

def midpoint(f, a, b, n):
    h = float(b-a)/n
    result = 0
    for i in range(n):
        val = (a + h/2.0) + i*h
        res = f(val)
        res1 = 3*val**2*exp(val**3)
        result += res
    result *= h
    return result
