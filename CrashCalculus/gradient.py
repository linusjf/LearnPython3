#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('gradient.pdf')
print("Setup Complete")

# Define the range for x and y
x = np.linspace(-10,10,1000)
xv, yv = np.meshgrid(x, x, indexing='ij')
 
# Compute f(x,y) = x^2 + y^3
zv = xv**2 + yv**3
 
# Plot the surface
fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(projection='3d')
ax.plot_surface(xv, yv, zv, cmap="viridis")
ax.set_title("f(x,y) = x² + y³")
pp.savefig()
pp.close()
