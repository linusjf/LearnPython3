#!/usr/bin/env python
# -*- coding: utf-8 -*-
from numpy import linspace

def midpoint(f, a, b, n):
    h = float(b-a)/n
    x = linspace(a + h/2, b - h/2, n)
    return h*sum(f(x))

