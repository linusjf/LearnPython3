#!/usr/bin/env python
# -*- coding: utf-8 -*-

# fit a straight line to the economic data
from numpy import sin
from numpy import sqrt
from numpy import arange
from pandas import read_csv
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

pp = PdfPages("curves.pdf")
print("Setup Complete")


# define the true objective function
def objective(x, a, b):
    return a * x + b


# load the dataset
url = "longley.csv"
dataframe = read_csv(url, header=None)
data = dataframe.values
# choose the input and output variables
x, y = data[:, 4], data[:, -1]

# curve fit
popt, _ = curve_fit(objective, x, y)
# summarize the parameter values
a, b = popt
print(f"y = {a:.5f} * x + {b:.5f}")
# plot input vs output
plt.scatter(x, y)
# define a sequence of inputs between the smallest and largest known inputs
x_line = arange(min(x), max(x), 1)
# calculate the output for the range
y_line = objective(x_line, a, b)
# create a line plot for the mapping function
plt.plot(x_line, y_line, "--", color="red")
pp.savefig()
plt.clf()


# define the true objective function
def objectivepoly(x, a, b, c):
    return a * x + b * x**2 + c


# curve fit
popt, _ = curve_fit(objectivepoly, x, y)
# summarize the parameter values
a, b, c = popt
print(f"y = {a:.5f} * x + {b:.5f} * x^2 + {c:.5f}")
# plot input vs output
plt.scatter(x, y)
# define a sequence of inputs between the smallest and largest known inputs
x_line = arange(min(x), max(x), 1)
# calculate the output for the range
y_line = objectivepoly(x_line, a, b, c)
# create a line plot for the mapping function
plt.plot(x_line, y_line, "--", color="red")
pp.savefig()
plt.clf()


# define the true objective function
def objectivefifth(x, a, b, c, d, e, f):
    return (a * x) + (b * x**2) + (c * x**3) + (d * x**4) + (e * x**5) + f


# curve fit
popt, _ = curve_fit(objectivefifth, x, y)
# summarize the parameter values
a, b, c, d, e, f = popt
print(f"y = {a:.5f} * x^5 + {b:.5f} * x^4 + {c:.5f} * x^3 + {d:.5f} * x^2 + {e:.5f} * x + {f:.5f}")
# plot input vs output
plt.scatter(x, y)
# define a sequence of inputs between the smallest and largest known inputs
x_line = arange(min(x), max(x), 1)
# calculate the output for the range
y_line = objectivefifth(x_line, a, b, c, d, e, f)
# create a line plot for the mapping function
plt.plot(x_line, y_line, "--", color="red")
pp.savefig()
plt.clf()


# define the true objective function
def objectivesin(x, a, b, c, d):
    return a * sin(b - x) + c * x**2 + d


# curve fit
popt, _ = curve_fit(objectivesin, x, y)
# summarize the parameter values
a, b, c, d = popt
print(f"y = {a:.5f} * sin({b:.5f} - x) + {c:.5f} * x^2 + {d:.5f}")
# plot input vs output
plt.scatter(x, y)
# define a sequence of inputs between the smallest and largest known inputs
x_line = arange(min(x), max(x), 1)
# calculate the output for the range
y_line = objectivesin(x_line, a, b, c, d)
# create a line plot for the mapping function
plt.plot(x_line, y_line, "--", color="red")
pp.savefig()
plt.clf()

pp.close()
