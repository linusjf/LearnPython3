#!/usr/bin/env python3
"""Tests == versus is."""
A = [1, 2, 3]
B = A

print(A is B)
print(A == B)
C = list(A)

print(A == C)
print(A is C)
