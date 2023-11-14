#!/usr/bin/env python
"""
Quartiles.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : quartiles
# @created     : Tuesday Nov 14, 2023 16:08:46 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages

pp = PdfPages("quartiles.pdf")
print("Setup Complete")
# creating dataset
np.random.seed(10)
data_1 = np.random.normal(100, 10, 200)
data_2 = np.random.normal(90, 20, 200)
data_3 = np.random.normal(80, 30, 200)
data_4 = np.random.normal(70, 40, 200)
data = [data_1, data_2, data_3, data_4]
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111)
bp = ax.boxplot(data, patch_artist=True, notch='True', vert=0)
colors = ['#FFFF00', '#66FF00', '#EE4B2B', '#0096FF']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
pp.savefig()
pp.close()
