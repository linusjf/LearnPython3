#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import linspace, zeros, sqrt, log
from trapezoidal import trapezoidal
from midpoint import midpoint
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

pp = PdfPages("adaptive.pdf")
print("Setup Complete")


def adaptive_integration(f, a, b, eps, method="midpoint"):
    # Just a choice (used to avoid inf loop)
    n_limit = 1000000
    n = 2
    if method == "trapezoidal":
        integral_n = trapezoidal(f, a, b, n)
        integral_2n = trapezoidal(f, a, b, 2 * n)
        diff = abs(integral_2n - integral_n)
        print("trapezoidal diff: ", diff)
        while (diff > eps) and (n < n_limit):
            integral_n = trapezoidal(f, a, b, n)
            integral_2n = trapezoidal(f, a, b, 2 * n)
            diff = abs(integral_2n - integral_n)
            print("trapezoidal diff: ", diff)
            n *= 2
    elif method == "midpoint":
        integral_n = midpoint(f, a, b, n)
        integral_2n = midpoint(f, a, b, 2 * n)
        diff = abs(integral_2n - integral_n)
        print("midpoint diff: ", diff)
        while (diff > eps) and (n < n_limit):
            integral_n = midpoint(f, a, b, n)
            integral_2n = midpoint(f, a, b, 2 * n)
            diff = abs(integral_2n - integral_n)
            print("midpoint diff: ", diff)
            n *= 2
    else:
        print("Error - adaptive integration called with unknown par")
    # Now we check if acceptable n was found or not
    if diff <= eps:  # Success
        print("The integral computes to: ", integral_2n)
        return n
    else:
        return -n  # Return negative n to tell "not found"


def application():
    """...Tasks b) and c)"""

    def f(x):
        return x**2

    def g(x):
        return sqrt(x)

    # eps = 1E-1           # Just switch between these two eps values
    eps = 1e-10
    # a = 0.0
    # If we adjust a, sqrt(x) is handled easily
    a = 0.0 + 0.01
    b = 2.0
    # ...f
    n = adaptive_integration(f, a, b, eps, "midpoint")
    if n > 0:
        print("Sufficient n is: %d" % (n))
    else:
        print("No n was found in %d iterations" % (n_limit))

    n = adaptive_integration(f, a, b, eps, "trapezoidal")
    if n > 0:
        print("Sufficient n is: %d" % (n))
    else:
        print("No n was found in %d iterations" % (n_limit))

    # ...g
    n = adaptive_integration(g, a, b, eps, "midpoint")
    if n > 0:
        print("Sufficient n is: %d" % (n))
    else:
        print("No n was found in %d iterations" % (n_limit))

    n = adaptive_integration(g, a, b, eps, "trapezoidal")
    if n > 0:
        print("Sufficient n is: %d" % (n))
    else:
        print("No n was found in %d iterations" % (n_limit))

    # Task c, make plot for both midpoint and trapezoidal
    eps = linspace(1e-1, 10e-10, 10)
    n_m = zeros(len(eps))
    n_t = zeros(len(eps))
    for i in range(len(n_m)):
        n_m[i] = adaptive_integration(g, a, b, eps[i], "midpoint")
        n_t[i] = adaptive_integration(g, a, b, eps[i], "trapezoidal")

    plt.plot(log(eps), n_m, "b-", log(eps), n_t, "r-")
    plt.xlabel("log(eps)")
    plt.ylabel("n for midpoint (blue) and trapezoidal (red)")
    plt.show()
    pp.savefig()
    pp.close()
    print(n)
    print(eps)


if __name__ == "__main__":
    application()
