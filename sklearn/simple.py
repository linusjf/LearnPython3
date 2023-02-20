#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(random_state=0)
# 2 samples, 3 features
X = [[1, 2, 3], [11, 12, 13]]
# classes of each sample
y = [0, 1]
clf.fit(X, y)

# predict classes of the training data
print("Predicted classes of training data:")
print(clf.predict(X))

print("Predicted classes of fresh data:")
# predict classes of new data
print(clf.predict([[14, 15, 16], [4, 5, 6]]))
