#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from scipy.stats import ttest_ind
from scipy.stats import kstest
from scipy.stats import normaltest
from scipy.stats import describe
from scipy.stats import skew,kurtosis

v1 = np.random.normal(size=100)
v2 = np.random.normal(size=100)

res = ttest_ind(v1, v2)

print(res)
print(res.pvalue)
v = np.random.normal(size=100)
res = kstest(v, 'norm')

print(res)
res = describe(v)
print(res)

v = np.random.normal(size=100)
print(skew(v))
print(kurtosis(v))

v = np.random.normal(size=100)
print(normaltest(v))

rng = np.random.default_rng()
pts = 1000
a = rng.normal(0, 1, size=pts)
b = rng.normal(2, 1, size=pts)
x = np.concatenate((a, b))
k2, p = normaltest(x)
alpha = 1e-3
print("p = {:g}".format(p))
# null hypothesis: x comes from a normal distribution
if p < alpha:  
    print("The null hypothesis can be rejected")
else:
    print("The null hypothesis cannot be rejected")
