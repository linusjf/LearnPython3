#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import array,mean,linspace
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('straight_line.pdf')
print("Setup Complete")

def f(t,a,b):
    return a*t + b

def find_error(a, b):
    E = 0
    for i in range(len(time)):
        E += (f(time[i],a,b) - data[i])**2
    return E

def line_fit():
    # Mean X and Y
    mean_x = mean(time)
    mean_y = mean(data)
    # Total number of values
    n = len(time)
    # Using the formula to calculate 'm' and 'c'
    numer = 0
    denom = 0
    for i in range(n):
        numer += (time[i] - mean_x) * (data[i] - mean_y)
        denom += (time[i] - mean_x) ** 2
    
    m = numer / denom
    c = mean_y - (m * mean_x)
    # Printing coefficients
    print("Coefficients")
    print(m, c)

    x = linspace(0,5,500)
    y = m * x + c
    # Plotting Line
    plt.plot(x, y, label="f(t)")
    # Plotting Scatter Points
    plt.plot(time, data,"*", c='#ef5423', label='y')
    plt.xlabel('Time (s)')
    plt.ylabel('y (stars) and straight line f(t)')
    plt.legend()
    plt.show()
    pp.savefig()
    plt.clf()

data = array([0.5, 2.0, 1.0, 1.5, 7.5])
time = array([0, 1, 2, 3, 4])

line_fit()
pp.close()
