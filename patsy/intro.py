#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

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
