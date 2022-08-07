#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('regression.pdf')
print("Setup Complete")
# Importing the csv file
origdf = pd.read_csv("auto-mpg.csv",
                     dtype={'mpg': 'float',
                            'weight': 'float','displacement': 'float'})
print(origdf.shape)
df = origdf[origdf.horsepower != "?"]
# Plotting the pairplot
sns.pairplot(df, diag_kind="kde")
pp.savefig()
plt.clf()
test = origdf[origdf.horsepower == "?"]
print(df.shape)
print(test.shape)
df["horsepower"] = pd.to_numeric(df["horsepower"], downcast="float")
X = df["weight"]
Y = df["horsepower"]
# here we are adding X_o = 1 to all the feature values 
X_b = np.c_[np.ones((df.shape[0],1)),X]
beta_values = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(Y)
print(beta_values)
X_new = test["weight"].values
print("Weights of cars: ",X_new)
X_new_b = np.c_[np.ones((test.shape[0],1)),X_new]
y_predict = X_new_b.dot(beta_values)
print("Predicted horsepower of cars: ",y_predict)
X_plot= np.array([[1500],[6000]])
X_plot_b = np.c_[np.ones((2,1)),X_plot] 
Y_plot = X_plot_b.dot(beta_values)
Equationline = "Y ={:.3f}+{:.3f}X".format(beta_values[0], beta_values[1])
plt.plot(X_plot, Y_plot, "r-", label = Equationline)
sns.scatterplot(x=X,y=Y, label = "Training Data")
plt.legend()
pp.savefig()
plt.clf()

reg = LinearRegression()
X = df["weight"]
Y = df["horsepower"]
X = X.values.reshape(-1,1)
Y = Y.values.reshape(-1,1)
reg.fit(X, Y)
print("The value obtained for beta_o is: ", reg.intercept_)
print("The value obtained for beta_1 is: ",reg.coef_)
print("Weights of cars: ",X_new)
print("Predicted horsepower of cars: ")
print(reg.predict(X_new.reshape(-1,1)))

#Selecting the variables of interest
X = df["horsepower"]
y = df["mpg"]
#Converting the series to a column matrix 
X_new = X.values.reshape(-1,1)
y_new = y.values.reshape(-1,1)

poly_features = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly_features.fit_transform(X_new)
reg = LinearRegression()
reg.fit(X_poly, y_new)
print("Y = {:.4f} X^2 {:.3f} X + {:.3f}".format(reg.coef_[0,1],reg.coef_[0,0], reg.intercept_[0]))
start = X.values.min()
stop = X.values.max()
X_plot = np.linspace(start, stop, 1000, dtype=float)
Y_plot = reg.coef_[0,1] * X_plot * X_plot + reg.coef_[0,0] * X_plot + reg.intercept_[0]
Equationline = "Y ={:.4f} $X^2$ {:.3f} $X$ + {:.3f}".format(reg.coef_[0,1], reg.coef_[0,0], reg.intercept_[0])
sns.scatterplot(x=X,y=y, label = "Training Data")
plt.plot(X_plot, Y_plot, "r-", label = Equationline)
plt.legend()
pp.savefig()
pp.close()
