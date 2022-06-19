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
pdf_pages.close()

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

# fix for dummy variable trap
X = X[:, 1:]
print(X[0])

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size = 0.2,random_state = 0)

from sklearn.linear_model import LinearRegression
model_fit = LinearRegression()
model_fit.fit(X_train,Y_train)
print(model_fit)

Y_pred = model_fit.predict(X_test)
print(Y_pred)

print(model_fit.coef_)
print(model_fit.intercept_)

from sklearn.metrics import r2_score
print(r2_score(Y_test,Y_pred))
