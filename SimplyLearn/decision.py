#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree

pd.set_option('display.max_columns', None)
bal_data = pd.read_csv("dtdata.csv",sep = ",", header = 0)
print("Data length: ", len(bal_data))
print("Data shape: ", bal_data.shape)
print("Balance data:")
print(bal_data.head())
