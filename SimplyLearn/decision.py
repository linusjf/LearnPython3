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

# Separating the data variables
X = bal_data.values[:, [0,1,2,3]]
Y = bal_data.values[:, 5]

# splitting data set into test and train
X_train,X_test,Y_train, Y_test = train_test_split(X,Y,test_size = 0.3, random_state = 100)

# Function to train on entropy
clf_entropy = DecisionTreeClassifier(criterion = "entropy", 
                                     random_state = 100,
                                     max_depth = 3,
                                     min_samples_leaf = 5)
clf_entropy.fit(X_train,Y_train)
Y_pred = clf_entropy.predict(X_test)

print("Accuracy is: {}".format(accuracy_score(Y_test,Y_pred) * 100))
