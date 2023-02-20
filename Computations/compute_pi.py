#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import pi, zeros, sqrt
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

pp = PdfPages("compute_pi.pdf")
print("Setup Complete")

no_of_terms = int(input("Give number of terms in sum for pi: "))
Leibniz_error = zeros(no_of_terms)
Euler_error = zeros(no_of_terms)

# Leibniz
sum1 = 0
for k in range(0, no_of_terms):
    sum1 += 1.0 / ((4 * k + 1) * (4 * k + 3))
    Leibniz_error[k] = pi - 8 * sum1
sum1 *= 8
final_Leibniz_error = abs(pi - sum1)
print("Leibniz: ", final_Leibniz_error)

# Euler
sum2 = 0
# Note index range
for k in range(1, no_of_terms + 1):
    sum2 += 1.0 / k**2
    Euler_error[k - 1] = pi - sqrt(6 * sum2)
sum2 *= 6
sum2 = sqrt(sum2)
final_Euler_error = abs(pi - sum2)
print("Euler: ", final_Euler_error)

plt.plot(range(no_of_terms), Leibniz_error, "b-", range(no_of_terms), Euler_error, "r-")
plt.xlabel("No of terms")
plt.ylabel("Error with Leibniz (blue) and Euler (red)")
plt.show()
pp.savefig()
pp.close()
