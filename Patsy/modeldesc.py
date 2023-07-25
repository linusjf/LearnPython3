#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from patsy import ModelDesc
from patsy import demo_data
from patsy import dmatrix, dmatrices

print(ModelDesc.from_formula("y ~ x").describe())
print(ModelDesc.from_formula("y ~ x + x + x").describe())
print(ModelDesc.from_formula("y ~ -1 + x").describe())
print(ModelDesc.from_formula("~ -1").describe())
print(ModelDesc.from_formula("y ~ a:b").describe())
print(ModelDesc.from_formula("y ~ a*b").describe())
print(ModelDesc.from_formula("y ~ (a + b + c + d) ** 2").describe())
print(ModelDesc.from_formula("y ~ (a + b)/(c + d)").describe())
print(ModelDesc.from_formula("np.log(x1 + x2) " "+ (x + {6: x3, 8 + 1: x4}[3 * i])").describe())
# Sometimes it might be easier to read if you put the processed formula back into formula notation using ModelDesc.describe():

desc = ModelDesc.from_formula("y ~ (a + b + c + d) ** 2")
print(desc.describe())

data = demo_data("a", "b", "x1", "x2")
mat = dmatrix("x1:x2 + a:b + b + x1:a:b + a + x2:a:x1", data)
print(mat.design_info.term_names)

data = demo_data("a", "b", "y")

mat1 = dmatrices("y ~ 0 + a:b", data)[1]

mat2 = dmatrices("y ~ 1 + a + b + a:b", data)[1]

np.linalg.matrix_rank(mat1)

print(np.linalg.matrix_rank(mat2))
print(np.linalg.matrix_rank(np.column_stack((mat1, mat2))))
print(mat1)
print(mat2)

print(dmatrices("y ~ 1", data)[1])
print(dmatrices("y ~ 1 + a", data)[1])
print(dmatrices("y ~ 1 + a + b", data)[1])
print(dmatrices("y ~ 1 + a + b + a:b", data)[1])
print(dmatrices("y ~ 1 + a:b", data)[1])
