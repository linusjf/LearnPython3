#!/usr/bin/env python
"""
Xonyandyonx.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : xonyandyonx
# @created     : Friday Oct 04, 2024 16:23:52 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
import numpy as np
from sklearn.linear_model import LinearRegression

# Generate data
np.random.seed(1)
x = np.random.rand(100)
noise = np.random.randn(100) / 1
print(np.std(noise))
y = 2 * x + noise

# Fit regressions
x_on_y = LinearRegression(fit_intercept=False).fit(y[:, np.newaxis], x)
y_on_x = LinearRegression(fit_intercept=False).fit(x[:, np.newaxis], y)

# Coefficient values
beta1 = y_on_x.coef_[0]
alpha1 = x_on_y.coef_[0]
print(beta1,alpha1)
# Verify inverse relationship
print(np.isclose(beta1 * alpha1, 1))  # Should print: True
