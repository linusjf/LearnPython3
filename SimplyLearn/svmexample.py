#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.datasets import make_blobs

# The PDF document
pdf_pages = PdfPages("svmexample.pdf")

# we create 40 separable points
X, Y = make_blobs(n_samples = 40, centers = 2, random_state = 2)

# fit the model, don't regularize for illustration purposes
clf = svm.SVC(kernel = 'linear', C=1000)
clf.fit(X,Y)
plt.scatter(X[:,0],X[:,1],c = Y,s = 30,cmap=plt.cm.Paired)
pdf_pages.savefig()
pdf_pages.close()
