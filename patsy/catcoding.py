#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from patsy import dmatrix, demo_data, ContrastMatrix, Poly

data = demo_data("a", nlevels=3)
print(data)
print(dmatrix("a", data))

l = ["a3", "a2", "a1"]

print(dmatrix("C(a, levels=l)", data))

print(dmatrix("C(a, Poly)", data))

contrast = [[1, 2], [3, 4], [5, 6]]
print(dmatrix("C(a, contrast)", data))
print(dmatrix("C(a, [[1], [2], [-4]])",data))

contrast_mat = ContrastMatrix(contrast, ["[pretty0]", "[pretty1]"])

print(dmatrix("C(a, contrast_mat)", data))

class MyTreat(object):
    def __init__(self, reference=0):
        self.reference = reference

    def code_with_intercept(self, levels):
        return ContrastMatrix(np.eye(len(levels)),
                              ["[My.%s]" % (level,) for level in levels])

    def code_without_intercept(self, levels):
        eye = np.eye(len(levels) - 1)
        contrasts = np.vstack((eye[:self.reference, :],
                               np.zeros((1, len(levels) - 1)),
                               eye[self.reference:, :]))
        suffixes = ["[MyT.%s]" % (level,) for level in
                    levels[:self.reference] + levels[self.reference + 1:]]
        return ContrastMatrix(contrasts, suffixes)

print(dmatrix("0 + C(a, MyTreat)", data))
# Reduced rank:
print(dmatrix("C(a, MyTreat)", data))

# With argument:
print(dmatrix("C(a, MyTreat(2))", data))
