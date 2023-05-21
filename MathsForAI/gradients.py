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
import sys
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from numpy import linalg
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
z = f(xvals, yvals)
print(z)
print(z.shape)

# pp.savefig()
pp.close()
