#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

pp = PdfPages("curvy2.pdf")
print("Setup Complete")

x = np.linspace(0, 10, num=40)
# The coefficients are much bigger.
a, b = (10.45, 5.334)
y = a * np.sin(b * x) + np.random.normal(size=40)
print(f"y = {a:.5f} * sin({b:.5f} * x) + e")


def test(x, a, b):
    return a * np.sin(b * x)


param, param_cov = curve_fit(test, x, y)

print("Sine function coefficients:")
print(param)
print("Covariance of coefficients:")
print(param_cov)

ans = param[0] * (np.sin(param[1] * x))
plt.plot(x, y, "o", color="red", label="data")
plt.plot(x, ans, "--", color="blue", label="optimized data")
plt.legend()
pp.savefig()
plt.clf()

pp.close()
