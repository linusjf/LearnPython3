#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import math
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score

dataset = pd.read_csv("diabetes.csv")
pd.set_option("display.max_columns", None)

print("Dataset length: ", len(dataset))
print(dataset.head())

# Replace zeroes
zero_not_accepted = ["Glucose", "BloodPressure", "Insulin", "SkinThickness", "BMI"]

for column in zero_not_accepted:
    dataset[column] = dataset[column].replace(0, np.NaN)
    mean = int(dataset[column].mean(skipna=True))
    dataset[column] = dataset[column].replace(np.NaN, mean)

# split dataset
X = dataset.iloc[:, 0:8]
Y = dataset.iloc[:, 8]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=0, test_size=0.2)

# Feature scaling
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

# Calculate value of k
print(math.sqrt(len(Y_test)))

# Define the model. Init KNN classifier
classifier = KNeighborsClassifier(n_neighbors=11, p=2, metric="euclidean")

# Fit model
classifier.fit(X_train, Y_train)

# predict the test values
Y_pred = classifier.predict(X_test)

# Evaluate model
cm = confusion_matrix(Y_test, Y_pred)
print(cm)
print(f1_score(Y_test, Y_pred))
print(accuracy_score(Y_test, Y_pred))
