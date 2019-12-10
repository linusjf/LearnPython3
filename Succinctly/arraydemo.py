#!/usr/bin/env python
"""Use numpy array."""
import sys
import numpy as np
A = np.array([4, 6, 8])
print(type(A))
A[0] = 7
print(A)
sys.exit()
