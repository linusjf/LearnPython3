#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from matplotlib.backends.backend_pdf import PdfPages

pp = PdfPages("regression.pdf")
print("Setup Complete")
# Importing the csv file
origdf = pd.read_csv(
    "auto-mpg.csv", dtype={"mpg": "float", "weight": "float", "displacement": "float"}
)
print(origdf.shape)
df = origdf[origdf.horsepower != "?"]
# Plotting the pairplot
sns.pairplot(df, diag_kind="kde")
pp.savefig()
plt.clf()
test = origdf[origdf.horsepower == "?"]
print(df.shape)
print(test.shape)
df = df.astype({"horsepower": "float"})
X = df["weight"]
Y = df["horsepower"]
# here we are adding X_0 = 1 to all the feature values
X_b = np.c_[np.ones((df.shape[0], 1)), X]
beta_values = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(Y)
print(beta_values)
X_new = test["weight"].values
print("Weights of cars: ", X_new)
X_new_b = np.c_[np.ones((test.shape[0], 1)), X_new]
y_predict = X_new_b.dot(beta_values)
print("Predicted horsepower of cars: ", y_predict)
X_plot = np.array([[1500], [6000]])
X_plot_b = np.c_[np.ones((2, 1)), X_plot]
Y_plot = X_plot_b.dot(beta_values)
Equationline = "Y ={:.3f}+{:.3f}X".format(beta_values[0], beta_values[1])
plt.plot(X_plot, Y_plot, "r-", label=Equationline)
sns.scatterplot(x=X, y=Y, label="Training Data")
plt.legend()
pp.savefig()
plt.clf()

reg = LinearRegression()
X = df["weight"]
Y = df["horsepower"]
X = X.values.reshape(-1, 1)
Y = Y.values.reshape(-1, 1)
reg.fit(X, Y)
print("The value obtained for beta_0 is: ", reg.intercept_)
print("The value obtained for beta_1 is: ", reg.coef_)
print("Weights of cars: ", X_new)
print("Predicted horsepower of cars: ")
print(reg.predict(X_new.reshape(-1, 1)))

# Selecting the variables of interest
X = df["horsepower"]
y = df["mpg"]
# Converting the series to a column matrix
X_new = X.values.reshape(-1, 1)
y_new = y.values.reshape(-1, 1)

poly_features = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly_features.fit_transform(X_new)
reg = LinearRegression()
reg.fit(X_poly, y_new)
print(
    "Y = {:.4f} X^2 {:.3f} X + {:.3f}".format(reg.coef_[0, 1], reg.coef_[0, 0], reg.intercept_[0])
)
start = X.values.min()
stop = X.values.max()
X_plot = np.linspace(start, stop, 1000, dtype=float)
Y_plot = reg.coef_[0, 1] * X_plot * X_plot + reg.coef_[0, 0] * X_plot + reg.intercept_[0]
Equationline = "Y ={:.4f} $X^2$ {:.3f} $X$ + {:.3f}".format(
    reg.coef_[0, 1], reg.coef_[0, 0], reg.intercept_[0]
)
sns.scatterplot(x=X, y=y, label="Training Data")
plt.plot(X_plot, Y_plot, "r-", label=Equationline)
plt.legend()
pp.savefig()

Y = df["displacement"]
X = df[["horsepower", "weight"]]
# Fitting the linear regression model
reg = LinearRegression()
reg.fit(X, Y)
# Printing the parameter values obtained after fitting the model
print("The value obtained for beta_0 is: ", reg.intercept_)
print("The value obtained for beta_1 and beta_2 are: ", reg.coef_[0], "and", reg.coef_[1])

# Plotting the surface plot
X1_min = df["horsepower"].values.min()
X1_max = df["horsepower"].values.max()
X1_values = np.linspace(X1_min, X1_max, 100)
X2_min = df["weight"].values.min()
X2_max = df["weight"].values.max()
X2_values = np.linspace(X2_min, X2_max, 100)
Y_reg = reg.intercept_ + (reg.coef_[0] * X1_values) + (reg.coef_[1] * X2_values)
Y_plot = Y_reg.reshape(-1, 1)
fig = plt.figure(figsize=(8.27, 11.69))
ax = fig.add_subplot(111, projection="3d")
ax.scatter(X.horsepower, X.weight, Y, color="red", s=1, label="Training data")
X1_plot, X2_plot = np.meshgrid(X1_values, X2_values)
surf = ax.plot_wireframe(X1_plot, X2_plot, Y_plot, rstride=10, cstride=10)
ax.view_init(50, 150)
ax.set_xlabel("Horsepower")
ax.set_ylabel("Weight")
ax.set_zlabel("Displacement")
ax.legend()
pp.savefig()
pp.close()
