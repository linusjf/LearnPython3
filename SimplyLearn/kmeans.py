#!/usr/bin/env python
# -*- coding: utf-8 -*-

from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import numpy as np

# The PDF document
pdf_pages = PdfPages("kmeans.pdf")
from sklearn.datasets import make_blobs
X, Y_true = make_blobs(n_samples = 300,centers = 4,cluster_std = 0.6,random_state = 0)
plt.scatter(X[:,0],X[:,1],s = 50)

pdf_pages.savefig()
pdf_pages.close()
