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

test, train = df[df['is_train'] == False], df[df['is_train'] == True]
print("Number of obs in training data: ",len(train))
print("Number of obs in test data: ",len(test))

features = df.columns[:4]
print(features)

y = pd.factorize(train['species'])[0]
print(y)

clf = RandomForestClassifier(n_jobs=2,random_state=0)
clf.fit(train[features],y)

#print(test[features])
pred = clf.predict(test[features])
#print(pred)
probs = clf.predict_proba(test[features])
print(probs)
preds = iris.target_names[pred]
print(preds[0:5])
print(test['species'].head())
cm = pd.crosstab(test['species'],preds,rownames=["Actual Species"],colnames=["Predicted Species"])
print(cm)
cmarray = cm.to_numpy()
print("Accuracy is : ", cmarray.trace()/cmarray.sum())
