#!/usr/bin/env python
"""
Linspace.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : linspace
# @created     : Sunday Nov 12, 2023 15:32:21 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

pp = PdfPages("linspace.pdf")
print("Setup Complete")

output = np.linspace(start=[2, 5, 9], stop=[100, 130, 160], num=10)
print(output)
print(output.shape)
print(output[0])
print(output[0][2])
output = np.linspace(start=[2, 5, 9],
                     stop=[100, 130, 160],
                     num=10,
                     axis=1)
print(output)
print(output.shape)
temperatures = [17.6, 18.9, 18.0, 18.9, 16.7, 14.3, 13.7, 13.8, 13.6, 15.7,
                18.6, 17.5, 18.4, 18.0, 17.2, 16.9, 16.8, 17.0, 15.9, 17.2,
                17.7, 16.9, 17.2, 17.8, 17.5, 16.9, 17.2]
plt.plot(temperatures)
plt.title("Temperatures along critical stretch (ºC)")
plt.ylabel("Temperature (ºC)")
plt.xlabel("List index")
pp.savefig()
position = np.linspace(17.5, 46.2, 27)
print(position)
plt.clf()
plt.plot(position, temperatures, marker='o', color="red")
plt.title("Temperatures along critical stretch (ºC)")
plt.ylabel("Temperature (ºC)")
plt.xlabel("Position on conveyor belt")
pp.savefig()

x_ = np.linspace(-5, 5, 5)
y_ = 4 * (x_**3) + 2 * (x_**2) + 5 * x_
plt.clf()
plt.plot(x_, y_)
pp.savefig()

x_ = np.linspace(-5, 5, 10)
y_ = 4 * (x_**3) + 2 * (x_**2) + 5 * x_
plt.clf()
plt.plot(x_, y_)
pp.savefig()

x_ = np.linspace(-5, 5, 100)
y_ = 4 * (x_**3) + 2 * (x_**2) + 5 * x_
plt.clf()
plt.plot(x_, y_)
pp.savefig()
pp.close()
