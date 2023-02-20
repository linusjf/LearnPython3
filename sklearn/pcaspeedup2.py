#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.decomposition import PCA

mnist = fetch_openml("mnist_784")
print("mnist fetched")
# test_size: what proportion of original data is used for test set
train_img, test_img, train_lbl, test_lbl = train_test_split(
    mnist.data, mnist.target, test_size=1 / 7.0, random_state=0
)

print("Training and test data created")
scaler = StandardScaler()
# Fit on training set only.
scaler.fit(train_img)
# Apply transform to both the training set and the test set.
train_img = scaler.transform(train_img)
test_img = scaler.transform(test_img)
print("Training and test data transformed")

# Make an instance of the Model
pca = PCA(0.95)

pca.fit(train_img)

train_img = pca.transform(train_img)
test_img = pca.transform(test_img)

print("Training and test data PCA transformed")
# all parameters not specified are set to their defaults
# default solver is incredibly slow which is why it was changed to 'lbfgs'
logisticRegr = LogisticRegression()

logisticRegr.fit(train_img, train_lbl)
print("Fit logistic regression")

# Predict for One Observation (image)
print("Single prediction")
print(logisticRegr.predict(test_img[0].reshape(1, -1)))
# Predict for One Observation (image)
print("Ten predictions")
print(logisticRegr.predict(test_img[0:10]))

print("Model score")
print(logisticRegr.score(test_img, test_lbl))
