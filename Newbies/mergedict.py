#!/usr/bin/env python3
"""Merge dicts."""
X = {'a': 1, 'b': 2}
Y = {'b': 3, 'c': 4}

Z = {**X, **Y}
print(Z)
Z = {**Y, **X}
print(Z)
