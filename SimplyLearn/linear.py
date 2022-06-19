#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import libraries
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)
# The PDF document
pdf_pages = PdfPages("linear.pdf")

companies = pd.read_csv("1000_companies.csv")
X = companies.iloc[:, :-1].values
Y = companies.iloc[:,4].values

print(companies.head())
print(X[0])
print(Y[0])

ax = sns.heatmap(companies.corr())
pdf_pages.savefig(bbox_inches='tight')

#Encoding categorical data
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
transformer = make_column_transformer(
    (OneHotEncoder(), ['State']),
    remainder='passthrough',
verbose_feature_names_out = False)
transformed = transformer.fit_transform(companies)
companies = pd.DataFrame(
    transformed, 
    columns=transformer.get_feature_names_out()
)
print(companies.head())
X = companies.iloc[:, :-1].values
Y = companies.iloc[:,6].values
print(X[0])
print(Y[0])

pdf_pages.close()
