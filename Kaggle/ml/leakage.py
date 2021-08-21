#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd

pd.set_option("display.max_rows", None)
pd.set_option("display.max_rows", None)
# Read the data
data = pd.read_csv('AER_credit_card_data.csv', 
                   true_values = ['yes'], false_values = ['no'])

# Select target
y = data.card

# Select predictors
X = data.drop(['card'], axis=1)

print("Number of rows in the dataset:", X.shape[0])
# more options can be specified also
with pd.option_context('display.max_rows', None, 'display.max_columns', None): 
    print(X.head())
