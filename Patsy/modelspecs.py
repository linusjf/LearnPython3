#!/usr/bin/env python
# -*- coding: utf-8 -*-

from patsy import dmatrix
from patsy import DesignMatrix, DesignInfo
from patsy import LookupFactor, ModelDesc, Term

X = [[1, 10], [1, 20], [1, -2]]
print(dmatrix(X))
design_info = DesignInfo(["Intercept!", "Not intercept!"])
X_dm = DesignMatrix(X, design_info)
print(dmatrix(X_dm))


def add_predictors(base_formula, extra_predictors):
    desc = ModelDesc.from_formula(base_formula)
    # Using LookupFactor here ensures that everything will work correctly even
    # if one of the column names in extra_columns is named like "weight.in.kg"
    # or "sys.exit()" or "LittleBobbyTables()".
    desc.rhs_termlist += [Term([LookupFactor(p)]) for p in extra_predictors]
    return desc


extra_predictors = [f"x{i}" for i in range(10)]
desc = add_predictors("np.log(y) ~ a*b + c:d", extra_predictors)
print(desc.describe())
