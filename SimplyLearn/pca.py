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

from sklearn.decomposition import PCA
pca = PCA(n_components=2)
pca.fit(scaled_data)
x_pca = pca.transform(scaled_data)
print(scaled_data.shape)
print(x_pca.shape)
# The PDF document
pdf_pages = PdfPages("pca.pdf")

plt.figure(figsize = (8,6))
plt.scatter(x_pca[:,0],x_pca[:,1],c=cancer['target'],cmap='plasma')
plt.xlabel("First principal component")
plt.ylabel("Second principal component")

pdf_pages.savefig()

print(pca.components_)
print(pca.explained_variance_ratio_)
df_comp = pd.DataFrame(pca.components_,columns=cancer["feature_names"])
plt.figure(figsize=(12,6))
sns.heatmap(df_comp,cmap='plasma')
pdf_pages.savefig(bbox_inches='tight')
pdf_pages.close()
