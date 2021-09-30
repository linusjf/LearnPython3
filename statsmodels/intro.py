#!/usr/bin/env python
# -*- coding: utf-8 -*-

import statsmodels.api as sm
import pandas
pandas.set_option('display.max_rows', 500)
pandas.set_option('display.max_columns', 500)
pandas.set_option('display.width', 1000)
from patsy import dmatrices
import matplotlib.pyplot as plt

df = sm.datasets.get_rdataset("Guerry", "HistData").data
vars = ['Department', 'Lottery', 'Literacy', 'Wealth', 'Region']
df = df[vars]
print(df[-5:])
df = df.dropna()
print(df[-5:])

y, X = dmatrices('Lottery ~ Literacy + Wealth + Region', data=df, return_type='dataframe')
print(y[:3])
print(X[:3])

# Describe model
mod = sm.OLS(y, X)    

# Fit model
res = mod.fit()       

# Summarize model
print(res.summary())  
print("Params")
print(res.params)   
print("Rsquared")
print(res.rsquared)
print("Rainbow test")
print(sm.stats.linear_rainbow(res))
print(sm.stats.linear_rainbow.__doc__)
sm.graphics.plot_partregress('Lottery', 'Wealth', ['Region', 'Literacy'],
                             data=df, obs_labels=False)
plt.savefig('intro.png')
