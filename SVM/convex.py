#!/usr/bin/env python
# -*- coding: utf-8 -*-
from succinctly.datasets import get_dataset, linearly_separable as ls
import cvxopt.solvers
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# The PDF document
pdf_pages = PdfPages("convex.pdf")

X, y = get_dataset(ls.get_training_examples)

m = X.shape[0]
print(X.shape)

# Gram matrix - The matrix of all possible inner products of X.
K = np.array([np.dot(X[i], X[j]) for j in range(m) for i in range(m)]).reshape((m, m))
P = cvxopt.matrix(np.outer(y, y) * K)
q = cvxopt.matrix(-1 * np.ones(m))
# Equality constraints
A = cvxopt.matrix(y, (1, m))
b = cvxopt.matrix(0.0)
# Inequality constraints
G = cvxopt.matrix(np.diag(-1 * np.ones(m)))
h = cvxopt.matrix(np.zeros(m))
# Solve the problem
solution = cvxopt.solvers.qp(P, q, G, h, A, b)
# Lagrange multipliers
multipliers = np.ravel(solution["x"])
# Support vectors have positive multipliers.
has_positive_multiplier = multipliers > 1e-7
sv_multipliers = multipliers[has_positive_multiplier]
print(sv_multipliers)
support_vectors = X[has_positive_multiplier]
print(support_vectors)
print(support_vectors.shape)
support_vectors_y = y[has_positive_multiplier]
print(support_vectors_y)
print(support_vectors_y.shape)


def compute_w(multipliers, X, y):
    return sum(multipliers[i] * y[i] * X[i] for i in range(len(y)))


w = compute_w(multipliers, X, y)
w_from_sv = compute_w(sv_multipliers, support_vectors, support_vectors_y)
# [0.44444446 1.11111114]
print(w)
# [0.44444453 1.11111128]
print(w_from_sv)


def compute_b(w, X, y):
    return np.sum([y[i] - np.dot(w, X[i]) for i in range(len(X))]) / len(X)


# -9.666668268506335
b = compute_b(w, support_vectors, support_vectors_y)
print(b)

plt.scatter(X[:, 0], X[:, 1], c=y, s=30, cmap=plt.cm.Paired)
pdf_pages.savefig()
ax = plt.gca()
xlim = ax.get_xlim()
print("xlim: ", xlim)
ylim = ax.get_ylim()
print("ylim: ", ylim)
xx = np.linspace(xlim[0], xlim[1], 30)
a = -w[0] / w[1]
yy = a * xx - (b) / w[1]
margin = 1 / np.sqrt(np.sum(w**2))
yy_neg = yy - np.sqrt(1 + a**2) * margin
yy_pos = yy + np.sqrt(1 + a**2) * margin
plt.figure(figsize=(8, 8))
plt.plot(xx, yy, "b-")
plt.plot(xx, yy_neg, "m--")
plt.plot(xx, yy_pos, "m--")
colors = ["steelblue", "orange"]
plt.scatter(
    X[:, 0], X[:, 1], c=y.ravel(), alpha=0.5, cmap=ListedColormap(colors), edgecolors="black"
)
plt.xlim(0, 12)
plt.ylim(0, 12)
pdf_pages.savefig()
pdf_pages.close()
