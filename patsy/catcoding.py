#!/usr/bin/env python
# -*- coding: utf-8 -*-

from patsy import dmatrix, demo_data, ContrastMatrix, Poly

data = demo_data("a", nlevels=3)
print(data)
print(dmatrix("a", data))

l = ["a3", "a2", "a1"]

print(dmatrix("C(a, levels=l)", data))

print(dmatrix("C(a, Poly)", data))
