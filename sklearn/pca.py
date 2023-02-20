#!/usr/bin/env python
# -*- coding: utf-8 -*-

# importing required libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from matplotlib.colors import ListedColormap
from matplotlib.colors import ListedColormap
from matplotlib.backends.backend_pdf import PdfPages

pp = PdfPages("pca.pdf")
from matplotlib.axes._axes import _log as matplotlib_axes_logger

matplotlib_axes_logger.setLevel("ERROR")
print("Setup Complete")

# importing or loading the dataset
dataset = pd.read_csv("wines.csv")
# distributing the dataset into two components X and Y
X = dataset.iloc[:, 0:13].values
y = dataset.iloc[:, 13].values

# Training set and Testing set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# performing preprocessing part
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Applying PCA function on training
# and testing set of X component
pca = PCA(n_components=2)
X_train = pca.fit_transform(X_train)
print(X_train.shape)
X_test = pca.transform(X_test)
print(X_test.shape)
explained_variance = pca.explained_variance_ratio_
print("pca explained variance: ", explained_variance)
# Fitting Logistic Regression To the training set
classifier = LogisticRegression(random_state=0)
classifier.fit(X_train, y_train)

# Predicting the test set result using
# predict function under LogisticRegression
y_pred = classifier.predict(X_test)

# making confusion matrix between
#  test set of Y and predicted value.
cm = confusion_matrix(y_test, y_pred)

# Predicting the training set
# result through scatter plot
X_set, y_set = X_train, y_train

X1, X2 = np.meshgrid(
    np.arange(start=X_set[:, 0].min() - 1, stop=X_set[:, 0].max() + 1, step=0.01),
    np.arange(start=X_set[:, 1].min() - 1, stop=X_set[:, 1].max() + 1, step=0.01),
)
plt.contourf(
    X1,
    X2,
    classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
    alpha=0.75,
    cmap=ListedColormap(("yellow", "white", "aquamarine")),
)

plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())

for i, j in enumerate(np.unique(y_set)):
    plt.scatter(
        X_set[y_set == j, 0],
        X_set[y_set == j, 1],
        c=ListedColormap(("red", "green", "blue"))(i),
        label=j,
    )
plt.title("Logistic Regression (Training set)")
# for Xlabel
plt.xlabel("PC1")
# for Ylabel
plt.ylabel("PC2")
# to show legend
plt.legend()
# show scatter plot
plt.show()
pp.savefig()
plt.clf()

# Visualising the Test set results through scatter plot
X_set, y_set = X_test, y_test
X1, X2 = np.meshgrid(
    np.arange(start=X_set[:, 0].min() - 1, stop=X_set[:, 0].max() + 1, step=0.01),
    np.arange(start=X_set[:, 1].min() - 1, stop=X_set[:, 1].max() + 1, step=0.01),
)

plt.contourf(
    X1,
    X2,
    classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
    alpha=0.75,
    cmap=ListedColormap(("yellow", "white", "aquamarine")),
)

plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())

for i, j in enumerate(np.unique(y_set)):
    plt.scatter(
        X_set[y_set == j, 0],
        X_set[y_set == j, 1],
        c=ListedColormap(("red", "green", "blue"))(i),
        label=j,
    )

# title for scatter plot
plt.title("Logistic Regression (Test set)")

# for Xlabel
plt.xlabel("PC1")
# for Ylabel
plt.ylabel("PC2")
plt.legend()

# show scatter plot
plt.show()
pp.savefig()
pp.close()
