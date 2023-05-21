#!/usr/bin/env python
"""
Gradients.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : gradients
# @created     : Sunday May 21, 2023 16:10:28 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# pylint: disable=invalid-name
# pylint: disable=unused-argument
import sys
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages

print(f"Python version {sys.version}")
print(f"Numpy version: {np.__version__}")
print(f"Matplotlib version: {matplotlib.__version__}")
pp = PdfPages("gradients.pdf")
print("Setup Complete")

# generate 2D meshgrid
nx, ny = (100, 100)
xvals = np.linspace(0, 10, nx)
yvals = np.linspace(0, 10, ny)

xv, yv = np.meshgrid(xvals, yvals)
print(xv, yv)


def f(x, y):
    """Define a function to plot."""
    return x * (y**2)


# calculate z value for x, y points
z = f(xv, yv)
print(z)
print(z.shape)

# draw a color plot to display the data
plt.figure(figsize=(14, 12))
plt.pcolor(xv, yv, z)
plt.title("2D plot for f(x, y) = xy^2")
plt.colorbar()
pp.savefig()

# generate 2D meshgrid for the gradient
nx, ny = (10, 10)
xvals = np.linspace(0, 10, nx)
yvals = np.linspace(0, 10, ny)

xg, yg = np.meshgrid(xvals, yvals)
# calculate the gradient of f(x,y)
Gy, Gx = np.gradient(f(xg, yg))
# draw a color plot to display the gradient
plt.figure(figsize=(14, 12))
plt.pcolor(xv, yv, z)
plt.title("2D plot for gradient of f(x, y) = xy^2")
plt.colorbar()
plt.quiver(xg, yg, Gx, Gy, scale=1000, color="w")
pp.savefig()


def ddx(x, y):
    """calculate the gradient of f(x,y) = xy^2"""
    return y**2


def ddy(x, y):
    """calculate the gradient of f(x,y) = xy^2"""
    return x * 2 * y


Gx = ddx(xg, yg)
Gy = ddx(xg, yg)
# draw a color plot to display the gradient
plt.figure(figsize=(14, 12))
plt.pcolor(xv, yv, z)
plt.title("plot of y^2 and 2xy")
plt.colorbar()
plt.quiver(xg, yg, Gx, Gy, scale=1000, color="w")
pp.savefig()

pp.close()
