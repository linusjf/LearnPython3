#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('regression.pdf')
print("Setup Complete")
# Importing the csv file
origdf = pd.read_csv("auto-mpg.csv")
print(origdf.shape)
df = origdf[origdf.horsepower != "?"]
# Plotting the pairplot
sns.pairplot(df, diag_kind="kde")
pp.savefig()
plt.clf()
test = origdf[origdf.horsepower == "?"]
print(df.shape)
print(test.shape)
X = df["weight"].astype(float)
#Y = df["horsepower"].astype(float)
Y = pd.to_numeric(df["horsepower"], downcast="float")
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
pp.close()
