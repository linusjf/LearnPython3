#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_validate

X, y = make_regression(n_samples=1000, random_state=0)
lr = LinearRegression()

result = cross_validate(lr, X, y)  # defaults to 5-fold CV
# r_squared score is high because dataset is easy
print(result["test_score"])

X, y = make_regression(n_samples=1000, random_state=0, noise=0.5)
result = cross_validate(lr, X, y)  # defaults to 5-fold CV
# r_squared score is high because dataset is easy
print(result["test_score"])
