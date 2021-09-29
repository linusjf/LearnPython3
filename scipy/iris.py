#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas
pandas.set_option('display.max_rows', 500)
pandas.set_option('display.max_columns', 500)
pandas.set_option('display.width', 1000)
from pandas import plotting
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('iris.pdf')
print("Setup Complete")

# Load the data
data = pandas.read_csv('iris.csv')
print(data.head())
print(data.describe())
model = ols('sepal_width ~ name + petal_length', data).fit()
print(model.summary())  

# Express the names as categories
categories = pandas.Categorical(data['name'])

# The parameter 'c' is passed to plt.scatter and will control the color
plotting.scatter_matrix(data, c=categories.codes, marker='o')

fig = plt.gcf()
fig.suptitle("blue: setosa, green: versicolor, red: virginica", size=13)

# Let us try to explain the sepal length as a function of the petal
# width and the category of iris

model = ols('sepal_width ~ name + petal_length', data).fit()
print(model.summary())

# Now formulate a "contrast", to test if the offset for versicolor and
# virginica are identical

print('Testing the difference between effect of versicolor and virginica')
print(model.f_test([0, 1, -1, 0]))
pp.savefig()
pp.close()
