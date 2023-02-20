#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from scipy.interpolate import UnivariateSpline
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

pp = PdfPages("gumbell.pdf")
print("Setup Complete")

years_nb = 21
wspeeds = np.load("sprog-windspeeds.npy")
print(wspeeds.shape)
max_speeds = np.array([arr.max() for arr in np.array_split(wspeeds, years_nb)])
print(max_speeds.shape)

plt.bar(np.arange(years_nb) + 1, max_speeds)
plt.axis("tight")
plt.xlabel("Year")
plt.ylabel("Annual wind speed maxima [$m/s$]")
pp.savefig()
plt.clf()


def gumbell_dist(arr):
    return -np.log(-np.log(arr))


sorted_max_speeds = np.sort(max_speeds)
cprob = (np.arange(years_nb, dtype=np.float32) + 1) / (years_nb + 1)
print(cprob)
gprob = gumbell_dist(cprob)
print(gprob)
speed_spline = UnivariateSpline(gprob, sorted_max_speeds, k=1)
nprob = gumbell_dist(np.linspace(1e-3, 1 - 1e-3, 100))
fitted_max_speeds = speed_spline(nprob)

fifty_prob = gumbell_dist(49.0 / 50.0)
print(fifty_prob)
fifty_wind = speed_spline(fifty_prob)
print(fifty_wind)

plt.plot(sorted_max_speeds, gprob, "o")
plt.plot(fitted_max_speeds, nprob, "g--")
plt.plot([fifty_wind], [fifty_prob], "o", ms=8.0, mfc="y", mec="y")
plt.plot([fifty_wind, fifty_wind], [plt.axis()[2], fifty_prob], "k--")
plt.text(35, -1, r"$V_{50} = %.2f \, m/s$" % fifty_wind)
plt.xlabel("Annual wind speed maxima [$m/s$]")
plt.ylabel("Gumbell cumulative probability")
pp.savefig()
plt.clf()

pp.close()
