#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('stats.pdf')
print("Setup Complete")

data = np.loadtxt('population.txt')
year, hares, lynxes, carrots = data.T # trick: columns to variables
plt.axes([0.2, 0.1, 0.5, 0.8])
plt.plot(year, hares, year, lynxes, year, carrots)
plt.legend(('Hare', 'Lynx', 'Carrot'), loc=(1.05, 0.5))
pp.savefig()
plt.clf()

print(data)
means = np.mean(data,axis=0,dtype=np.float64)
print(means[1:])
stds = np.std(data,axis=0,dtype=np.float64)
print(stds[1:])

largest = np.amax(data,axis=0)
print(largest)
year1 = np.where(data[:,1] == largest[1])
print(data[np.ravel(year1)[0]][0])
year2 = np.where(data[:,2] == largest[2])
print(data[np.ravel(year2)[0]][0])
year3 = np.where(data[:,3] == largest[3])
print(data[np.ravel(year3)[0]][0])

largest = np.argmax(data[:,1:], axis=1)
print(largest)
cats = np.array(['Hare','Lynx','Carrot'])
print(cats[largest].reshape(len(largest),1))
plus = np.any(data[:,1:] > 50000,axis=1)
plusyears = data[:,0][plus]
print(plusyears.reshape(len(plusyears),1))
pp.close()
