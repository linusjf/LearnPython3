#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import statsmodels.api as sm

data = sm.datasets.longley.load()
print(data.names)
print(data.endog_name)
print(data.exog_name)
data.exog = sm.add_constant(data.exog)
results = sm.OLS(data.endog, data.exog).fit()
A = np.identity(len(results.params))
A = A[1:, :]
print(A)
# This tests that each coefficient is jointly statistically significantly different from zero.
print(results.f_test(A))

print(results.fvalue)
# 330.2853392346658
print(results.f_pvalue)
# 4.98403096572e-10
B = np.array(([0, 0, 1, -1, 0, 0, 0], [0, 0, 0, 0, 0, 1, -1]))
# This tests that the coefficient on the 2nd and 3rd regressors are equal and jointly that the coefficient on the 5th and 6th regressors are equal.
print(results.f_test(B))

from statsmodels.datasets import longley
from statsmodels.formula.api import ols

dta = longley.load_pandas().data
print(dta.describe())
formula = "TOTEMP ~ GNPDEFL + GNP + UNEMP + ARMED + POP + YEAR"
results = ols(formula, dta).fit()
hypotheses = "(GNPDEFL = GNP), (UNEMP = 2), (YEAR/1829 = 1)"
print(hypotheses)
f_test = results.f_test(hypotheses)
print(f_test)
hypotheses = "(GNPDEFL = GNP), (UNEMP = 2)"
print(hypotheses)
f_test = results.f_test(hypotheses)
print(f_test)
hypotheses = "(GNPDEFL = GNP),(YEAR/1829 = 1)"
print(hypotheses)
f_test = results.f_test(hypotheses)
print(f_test)
hypotheses = "(UNEMP = 2), (YEAR/1829 = 1)"
print(hypotheses)
f_test = results.f_test(hypotheses)
print(f_test)
hypotheses = "(UNEMP = 2)"
print(hypotheses)
f_test = results.f_test(hypotheses)
print(f_test)
hypotheses = "(YEAR/1829 = 1)"
print(hypotheses)
f_test = results.f_test(hypotheses)
print(f_test)
hypotheses = "(GNPDEFL = GNP)"
print(hypotheses)
f_test = results.f_test(hypotheses)
print(f_test)
