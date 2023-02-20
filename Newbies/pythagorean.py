#!/usr/bin/env python3
"""Pythagorean triplets."""
from math import sqrt

N = input("Maximum Number? ")
print()
print("Number input: " + N)
N = int(N) + 1
for a in range(1, N):
    for b in range(a, N):
        c_square = a**2 + b**2
        c = int(sqrt(c_square))
        if c_square - c**2 == 0:
            print(a, b, c)
