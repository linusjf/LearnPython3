#!/usr/bin/env python
# -*- coding: utf-8 -*-

from statsmodels.formula.api import ols
import pandas
pandas.set_option('display.max_rows', 500)
pandas.set_option('display.max_columns', 500)
pandas.set_option('display.width', 1000)
from pandas import plotting
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('brainsize.pdf')
print("Setup Complete")


data = pandas.read_csv('brain_size.csv', sep=';', na_values=".")
print(data)

t = np.linspace(-6, 6, 20)
sin_t = np.sin(t)
cos_t = np.cos(t)
df = pandas.DataFrame({'t': t, 'sin': sin_t, 'cos': cos_t})  
print(df)

# 40 rows and 8 columns
print(data.shape)
# It has columns   
print(data.columns)

# Columns can be addressed by name   
print(data['Gender'])  

# Simpler selector
meanFViq = data[data['Gender'] == 'Female']['VIQ'].mean()
print(meanFViq)

groupby_gender = data.groupby('Gender')
for gender, value in groupby_gender['VIQ']:
    print((gender, value.mean()))
print(groupby_gender.mean())

groupby_gender.boxplot(column=['FSIQ', 'VIQ', 'PIQ'])
pp.savefig()
plt.clf()

# Scatter matrices for different columns
plotting.scatter_matrix(data[['Weight', 'Height', 'MRI_Count']])
pp.savefig()
plt.clf()
plotting.scatter_matrix(data[['PIQ', 'VIQ', 'FSIQ']])
pp.savefig()
# Scatter matrices for different columns
plotting.scatter_matrix(data[data['Gender'] == 'Male'][['PIQ', 'VIQ', 'FSIQ']])
pp.savefig()
plt.clf()
plotting.scatter_matrix(data[data['Gender'] == 'Female'][['PIQ', 'VIQ', 'FSIQ']])
pp.savefig()
plt.clf()

pp.close()

res = stats.ttest_1samp(data['VIQ'], 0)   
print(res)
female_viq = data[data['Gender'] == 'Female']['VIQ']
male_viq = data[data['Gender'] == 'Male']['VIQ']
res = stats.ttest_ind(female_viq, male_viq)   
print(res)
res = stats.ttest_ind(data['FSIQ'], data['PIQ'])   
print(res)
res = stats.ttest_rel(data['FSIQ'], data['PIQ'])   
print(res)
res = stats.ttest_1samp(data['FSIQ'] - data['PIQ'], 0)   
print(res)
res = stats.wilcoxon(data['FSIQ'], data['PIQ'])   
print(res)
males = data[data['Gender'] == 'Male']
females = data[data['Gender'] == 'Female']
maleWts = males['Weight']
femaleWts = females['Weight']
res = stats.ttest_rel(maleWts, femaleWts,nan_policy='omit')   
print(res)
maleVIQ = males['VIQ']
femaleVIQ = females['VIQ']
res = stats.mannwhitneyu(maleVIQ, femaleVIQ)   
print(res)

model = ols("VIQ ~ Gender + 1", data).fit()
print(model.summary())
