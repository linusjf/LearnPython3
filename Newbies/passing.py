#!/usr/bin/env python3
"""Passing functions as objects."""
def myfunc(_a, _b):
    """Add two numbers."""
    return _a + _b

FUNCS = [myfunc]
print(FUNCS[0])
print(FUNCS[0](2, 3))
