#!/usr/bin/env python
# -*- coding: utf-8 -*-
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import pandas as pd; pd.set_option('display.max_columns', None)
import numpy as np
import seaborn as sns

from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()
print(cancer.keys())
print(cancer['target_names'])
print(cancer['feature_names'])
df = pd.DataFrame(cancer['data'],columns=cancer['feature_names'])
print(df.head())

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(df)
scaled_data = scaler.transform(df)
# The PDF document
pdf_pages = PdfPages("pca.pdf")

fig = plt.figure(figsize = (6,4))
pdf_pages.savefig()
pdf_pages.close()
