#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sklearn.datasets import load_iris

from sklearn.ensemble import RandomForestClassifier

import pandas as pd
pd.set_option('display.max_columns', None)

import numpy as np

np.random.seed(0)

iris = load_iris()
#print(iris)
#print(iris.DESCR)

df = pd.DataFrame(iris.data, columns = iris.feature_names)

print(df.head())

df['species'] = pd.Categorical.from_codes(iris.target,iris.target_names)
print(df.head())

df['is_train'] = np.random.uniform(0,1, len(df.index)) <= 0.75
print(df.head())

