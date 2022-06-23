#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sklearn.datasets import load_iris

from sklearn.ensemble import RandomForestClassifier

import pandas as pd
pd.set_option('display.max_columns', None)

import numpy as np

np.random.seed(0)

iris = load_iris()

df = pd.DataFrame(iris.data, columns = iris.feature_names)

print(df.head())
