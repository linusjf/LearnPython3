#!/usr/bin/env python
# -*- coding: utf-8 -*-

import warnings
from sympy import *
q = Symbol("q", positive = True)
m = Matrix([
[-2*cosh(q/3),      exp(-q),            1],
[      exp(q), -2*cosh(q/3),            1],
[           1,            1, -2*cosh(q/3)]])
print(m.nullspace()) 

def my_iszero(x):
    try:
        result = x.is_zero
    except AttributeError:
        result = None

    # Warnings if evaluated into None
    if result is None:
        warnings.warn("Zero testing of {} evaluated into None".format(x))
    return result

print(m.nullspace(iszerofunc=my_iszero)) 

def my_iszeroA(x):
    try:
        result = x.rewrite(exp).simplify().is_zero
    except AttributeError:
        result = None

    # Warnings if evaluated into None
    if result is None:
        warnings.warn("Zero testing of {} evaluated into None".format(x))
    return result

print(m.nullspace(iszerofunc=my_iszeroA)) 
