#!/usr/bin/env python
# -*- coding: utf-8 -*-
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()
print(cancer.keys())

# The PDF document
pdf_pages = PdfPages("pca.pdf")

fig = plt.figure(figsize = (6,4))
pdf_pages.savefig()
pdf_pages.close()
