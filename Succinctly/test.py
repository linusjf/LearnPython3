#!/usr/bin/env python
"""Test numpy and scipy."""
import numpy as np

print("\nHello from test.py")

A = np.array([2, 4, 6, 8])
print(A)
LENGTH = A.size  # 4
A[LENGTH - 1] = 9
print(A)
print("Goodbye from test.py")
