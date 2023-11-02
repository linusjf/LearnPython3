#!/usr/bin/env python
"""
Normalize.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : normalize
# @created     : Thursday Nov 02, 2023 09:35:45 IST
# @description : Example of rescaling, normalizing and standardizing
# -*- coding: utf-8 -*-'
######################################################################
"""
import pandas as pd
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import RobustScaler
cols = ['loan_amount', 'interest_rate', 'installment']
data = pd.read_csv('loans_full_schema.csv', nrows = 30000, usecols = cols)
print(data)

# Standardization
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)
print(data_scaled.mean(axis=0))
print(data_scaled.std(axis=0))
print('Min values (Loan Amount, Int rate and Installment): ', data_scaled.min(axis=0))
print('Max values (Loan Amount, Int rate and Installment): ', data_scaled.max(axis=0))

# Normalization
scaler = MinMaxScaler()
data_scaled = scaler.fit_transform(data)
print('means (Loan Amount, Int rate and Installment): ', data_scaled.mean(axis=0))
print('std (Loan Amount, Int rate and Installment): ', data_scaled.std(axis=0))
print('Min (Loan Amount, Int rate and Installment): ', data_scaled.min(axis=0))
print('Max (Loan Amount, Int rate and Installment): ', data_scaled.max(axis=0))

# Rescaling
# Robust Scalar (Scaling to median and quantiles) :
# Scaling using median and quantiles consists of subtracting
# the median to all the observations and then dividing by the
# interquartile difference. It Scales features using statistics that are robust to
# outliers.
# The interquartile difference is the difference between the 75th and 25th quantile:
# IQR = 75th quantile — 25th quantile
# The equation to calculate scaled values:
# X_scaled = (X — X.median) / IQR
scaler = RobustScaler()
data_scaled = scaler.fit_transform(data)
print('means (Loan Amount, Int rate and Installment): ', data_scaled.mean(axis=0))
print('std (Loan Amount, Int rate and Installment): ', data_scaled.std(axis=0))
print('Min (Loan Amount, Int rate and Installment): ', data_scaled.min(axis=0))
print('Max (Loan Amount, Int rate and Installment): ', data_scaled.max(axis=0))
