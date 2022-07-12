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

# Define the range for x and y
x = np.linspace(-10,10,20)
xv, yv = np.meshgrid(x, x, indexing='ij')
 
# Compute the gradient of f(x,y)
fx = 2*xv
fy = 3*yv*yv
 
# Convert the vector (fx,fy) into size and direction
size = np.sqrt(fx**2 + fy**2)
dir_x = fx/size
dir_y = fy/size
 
# Plot the surface
plt.figure(figsize=(6,6))
plt.quiver(xv, yv, dir_x, dir_y, size, cmap="viridis")
pp.savefig()
pp.close()

def f(x, y):
    return x**2 + y**3
 
# 0 to 360 degrees at 0.1-degree steps
angles = np.arange(0, 360, 0.1)
 
# coordinate to check
x, y = 2, 3
# step size for differentiation
step = 0.0001
 
# To keep the size and direction of maximum rate of change
maxdf, maxangle = -np.inf, 0
for angle in angles:
    # convert degree to radian
    rad = angle * np.pi / 180
    # delta x and delta y for a fixed step size
    dx, dy = np.sin(rad)*step, np.cos(rad)*step
    # rate of change at a small step
    df = (f(x+dx, y+dy) - f(x,y))/step
    # keep the maximum rate of change
    if df > maxdf:
        maxdf, maxangle = df, angle
 
# Report the result
dx, dy = np.sin(maxangle*np.pi/180), np.cos(maxangle*np.pi/180)
gradx, grady = dx*maxdf, dy*maxdf
print(f"Max rate of change is at {maxangle} degrees")
print(f"Gradient vector at ({x},{y}) is ({dx*maxdf},{dy*maxdf})")
print(f"Gradient vector by formula at ({x},{y}) is ({2*x},{3*y**2})")
