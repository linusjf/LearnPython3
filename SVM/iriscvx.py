#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import pandas as pd; pd.set_option('display.max_columns', None) 
import numpy as np
from cvxopt import matrix, solvers
from sklearn.datasets import load_iris
iris = load_iris()
iris_df = pd.DataFrame(data= np.c_[iris["data"], iris["target"]], columns= iris["feature_names"] + ["target"])
# Retain only 2 linearly separable classes
iris_df = iris_df[iris_df["target"].isin([0,1])]
iris_df["target"] = iris_df[["target"]].replace(0,-1)
# Select only 2 attributes
iris_df = iris_df[["petal length (cm)", "petal width (cm)", "target"]]
print(iris_df.head())

X = iris_df[["petal length (cm)", "petal width (cm)"]].to_numpy()
y = iris_df[["target"]].to_numpy()
# The PDF document
pdf_pages = PdfPages("iriscvx.pdf")
plt.figure(figsize=(8, 8))
colors = ["steelblue", "orange"]
plt.scatter(X[:, 0], X[:, 1], c=y.ravel(), alpha=0.5, cmap=matplotlib.colors.ListedColormap(colors), edgecolors="black")
pdf_pages.savefig()

n = X.shape[0]
H = np.dot(y*X, (y*X).T)
q = np.repeat([-1.0], n)[..., None]
A = y.reshape(1, -1)
b = 0.0
G = np.negative(np.eye(n))
h = np.zeros(n)

P = matrix(H)
q = matrix(q)
G = matrix(G)
h = matrix(h)
A = matrix(A)
b = matrix(b)
sol = solvers.qp(P, q, G, h, A, b)
alphas = np.array(sol["x"])
w = np.dot((y * alphas).T, X)[0]
S = (alphas > 1e-5).flatten()
b = np.mean(y[S] - np.dot(X[S], w.reshape(-1,1)))

print("W:", w)
print("b:", b)

from sklearn import svm
# Use the linear kernel and set C to a large value to ensure hard margin fitting
clf = svm.SVC(kernel="linear", C=10.0)
clf.fit(X, y.ravel())
w = clf.coef_[0]
b = clf.intercept_
print("W:", w)
print("b:", b)

x_min = 0
x_max = 5.5
y_min = 0
y_max = 2
xx = np.linspace(x_min, x_max)
a = -w[0]/w[1]
yy = a*xx - (b)/w[1]
margin = 1 / np.sqrt(np.sum(w**2))
yy_neg = yy - np.sqrt(1 + a**2) * margin
yy_pos = yy + np.sqrt(1 + a**2) * margin
plt.figure(figsize=(8, 8))
plt.plot(xx, yy, "b-")
plt.plot(xx, yy_neg, "m--")
plt.plot(xx, yy_pos, "m--")
colors = ["steelblue", "orange"]
plt.scatter(X[:, 0], X[:, 1], c=y.ravel(), alpha=0.5, cmap=matplotlib.colors.ListedColormap(colors), edgecolors="black")
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
pdf_pages.savefig()
pdf_pages.close()
