#!/usr/bin/env python
"""
Lawoflargenos.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : lawoflargenos
# @created     : Monday Oct 02, 2023 10:24:02 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
import random
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages

pp = PdfPages("lawoflargenos.pdf")
print("Setup Complete")

N = 1
prob = []
flip = []

while N < 1000:
    HEAD = 0
    TAIL = 0

    for i in range(N):
        if random.randint(0, 1) == 0:
            HEAD += 1
        else:
            TAIL += 1
    k = HEAD / (HEAD + TAIL)
    prob.append(k)
    flip.append(N)
    N += 1

plt.figure(figsize=(20, 10))
plt.subplot(2, 1, 1)
plt.hist(prob, 100, label="Probability of Heads")
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(flip, prob)
plt.xlabel("Number of Flips")
plt.ylabel("Probability of Heads")
plt.grid(True)
pp.savefig()
plt.clf()

# create population with a gamma distribution
shape, scale = 2.0, 2.0  # mean=4, std=2*sqrt(2)
s = np.random.gamma(shape, scale, 1000000)

# Step 2
samplemeanlist = []  # list of sample mean
lst = []  # list of sample size, for x-axis of box plots
numberofsample = 50  # number of sample in each sample size
# set sample size (i) between 100 to 8100, step by 500
for i in range(100, 8101, 500):
    # set x-axis
    lst.append(i)
    # list of mean of each sample
    ml = []
    # sample 50 time.
    for n in range(0, numberofsample):
        # random pick from population with sample size = i
        rs = random.choices(s, k=i)
        # calculate the mean of each sample and save it in list of mean
        ml.append(sum(rs) / i)

    # save the 50 sample mean in samplemeanlist for box plots
    samplemeanlist.append(ml)

# Step 3
# set figure size
boxplots = plt.figure(figsize=(20, 10))
# plot box plots of each sample mean
plt.boxplot(samplemeanlist, labels=lst)
pp.savefig()
plt.clf()

print(
    "sample with 100 sample size,"
    + "mean:"
    + str(np.mean(samplemeanlist[0]))
    + ", standard deviation: "
    + str(np.std(samplemeanlist[0]))
)
print(
    "sample with 8100 sample size,"
    + "mean:"
    + str(np.mean(samplemeanlist[16]))
    + ", standard deviation: "
    + str(np.std(samplemeanlist[16]))
)

# last hist plot
histplot = plt.figure(figsize=(20, 10))
plt.hist(samplemeanlist[0], 10, density=True)
plt.hist(samplemeanlist[16], 10, density=True)
pp.savefig()
plt.clf()

pp.close()
