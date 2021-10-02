#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import uniform
import numpy as np
import matplotlib.pyplot as plt
from patsy import build_design_matrices,dmatrix
from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('bspline.pdf')
print("Setup Complete")

x = np.linspace(0., 1., 100)
y = dmatrix("bs(x, df=6, degree=3, include_intercept=True) - 1", {"x": x})
print("y")
print(y.shape)

for i in range(3):
    # Define some coefficients
    #b = np.array([1.3, 0.6, 0.9, 0.4, 1.6, 0.7])

    # Define random coefficients in range 0 - 2
    a1 = uniform(0,2)
    a2 = uniform(0,2)
    a3 = uniform(0,2)
    a4 = uniform(0,2)
    a5 = uniform(0,2)
    a6 = uniform(0,2)
    b = np.array([a1,a2,a3,a4,a5,a6])
    print("b")
    print(b)

    # Plot B-spline basis functions (colored curves) each multiplied by its coeff
    print("y*b")
    print((y*b).shape)
    plt.title("B-spline basis example (degree=3)");
    plt.plot(x, y*b);

    # Plot the spline itself (sum of the basis functions, thick black curve)
    print("y.b")
    print(np.dot(y,b).shape)
    plt.plot(x, np.dot(y, b), color='k', linewidth=3);
    pp.savefig()
    plt.clf()

pp.close()
#plt.savefig("bspline.png")

data = {"x": np.linspace(0., 1., 100)}

design_matrix = dmatrix("bs(x, df=4)", data)

new_data = {"x": [0.1, 0.25, 0.9]}

d = build_design_matrices([design_matrix.design_info], new_data)[0]
print(d)

plt.clf()
plt.title("Natural cubic regression spline basis example");

y = dmatrix("cr(x, df=6) - 1", {"x": x})

# Plot natural cubic regression spline basis functions (colored curves) each multiplied by its coeff
plt.plot(x, y*b);

# Plot the spline itself (sum of the basis functions, thick black curve)
plt.plot(x, np.dot(y, b), color='k', linewidth=3);
plt.savefig("natural.png")
plt.clf()
plt.title("Cyclic cubic regression spline basis example");

y = dmatrix("cc(x, df=6) - 1", {"x": x})

# Plot cyclic cubic regression spline basis functions (colored curves) each multiplied by its coeff
plt.plot(x, y*b);

# Plot the spline itself (sum of the basis functions, thick black curve)
plt.plot(x, np.dot(y, b), color='k', linewidth=3);
plt.savefig("cyclic.png")

new_design_matrix = build_design_matrices([design_matrix.design_info], new_data)[0]

print(new_design_matrix)
print(np.asarray(new_design_matrix))
