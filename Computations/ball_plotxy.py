#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import linspace,pi,cos,sin
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d as plt3d
from mpl_toolkits.mplot3d import axes3d
from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('ball_plotxy.pdf')
print("Setup Complete")

theta = pi/4
v0 = 5
vx = sin(theta) * v0
vy = cos(theta) * v0
g = 9.81
t = linspace(0, 1, 1001)

x = vx*t
y = vy*t - 0.5*g*t**2

# Creating figure
fig = plt.figure(figsize = (10, 7))
ax = plt.axes(projection='3d')
ax.plot(x, y,t,label = "Position in time")
plt.xlabel('x (m)')
plt.ylabel('y (m)')
ax.set_zlabel('t (s)')
plt.show()
pp.savefig()
plt.clf()
fig = plt.figure(figsize = (10, 7))
plt.plot(x, y)
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.show()
pp.savefig()

pp.close()
