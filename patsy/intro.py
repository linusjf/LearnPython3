#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import patsy
from patsy import dmatrices, dmatrix, demo_data

data = demo_data("a", "b", "x1", "x2", "y", "z column")

print(data)

matrix = dmatrices("y ~ x1 + x2", data)
print(matrix)

outcome, predictors = dmatrices("y ~ x1 + x2", data)
print(outcome)
print(predictors)
betas = np.linalg.lstsq(predictors, outcome,rcond=None)[0].ravel()
print(betas)
for name, beta in zip(predictors.design_info.column_names, betas):
    print(f"{name}: {beta}")


d = dmatrix("x1 + x2", data)
print(d)
d = dmatrix("x1 + x2 - 1", data)
print(d)
d = dmatrix("x1 + np.log(x2 + 10)", data)
print(d)
new_x2 = data["x2"] * 100
d = dmatrix("new_x2")
print(d)
d = dmatrix("center(x1) + standardize(x2)", data)
print(d)
print(dir(patsy.builtins))
def double(x):
    return 2 * x

d = dmatrix("x1 + double(x1)", data)
print(d)

weird_data = demo_data("weird column!", "x1")

# This is an error...
try:
    dmatrix("weird column! + x1", weird_data)
except patsy.PatsyError as pe:
    print(f"{pe}")

# ...but this works:
d = dmatrix("Q('weird column!') + x1",weird_data)
print(d)

# compare to "x1 + x2"
d = dmatrix("I(x1 + x2)", data)  
print(d)

d = dmatrix("I(x1 + x2)", {"x1": np.array([1, 2, 3]), "x2": np.array([4, 5, 6])})
print(d)

d = dmatrix("I(x1 + x2)", {"x1": [1, 2, 3], "x2": [4, 5, 6]})
print(d)

d = dmatrix("0 + a", data)
print(d)

d = dmatrix("a", data)
print(d)

d = dmatrix("0 + a:b", data)
print(d)

d = dmatrix("a + b + a:b", data)
print(d)

d = dmatrix("a*b", data)
print(d)

d = dmatrix("C(c, Poly)", {"c": ["c1", "c1", "c2", "c2", "c3", "c3"]})
print(d)

d = dmatrix("a:x1", data)
print(d)

d = dmatrix("x1 + a:x1", data)
print(d)

d = dmatrix("C(a, Poly):center(x1)", data)
print(d)
