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
print("X: ",X)
print("Y: ",Y)
# fit the model, don't regularize for illustration purposes
clf = svm.SVC(kernel = 'linear', C=1000)
clf.fit(X,Y)
plt.scatter(X[:,0],X[:,1],c = Y,s = 30,cmap=plt.cm.Paired)
pdf_pages.savefig()

newdata = [[3,4],[5,6]]
print("predicted: ",clf.predict(newdata))

plt.scatter(X[:,0],X[:,1],c = Y,s = 30,cmap=plt.cm.Paired)

# plot the decision function
ax = plt.gca()
xlim = ax.get_xlim()
ylim = ax.get_ylim()
xx = np.linspace(xlim[0],xlim[1],30)
yy = np.linspace(ylim[0],ylim[1],30)
YY, XX = np.meshgrid(yy,xx)
xy = np.vstack([XX.ravel(),YY.ravel()]).T
Z = clf.decision_function(xy).reshape(XX.shape)
ax.contour(XX,YY,Z,colors='k',levels=[-1,0,1],
           alpha=0.5,
           linestyles=['--','-','--'])
ax.scatter(clf.support_vectors_[:,0],
           clf.support_vectors_[:,1],
           s=100,
           linewidth=1,
           facecolors='none')

pdf_pages.savefig()
pdf_pages.close()
