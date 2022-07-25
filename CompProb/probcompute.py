#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Import packages with the functions we need
import scipy.special
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('probcompute.pdf')
print("Setup Complete")

probabilities = []

for n in range(51):
    # Calculate probability of n heads
    probability = scipy.special.binom(50, n) / (2 ** 50)
    # Convert to a string with 6 decimal places
    probString = "{:.15f}".format(probability)
    # Print probability
    print('Prob of ' + str(n) + ' heads: ' + probString)
    # Add probability to list
    probabilities.append(probability)

# Plot the probabilites
plt.plot(range(51), probabilities, '-o')
plt.axis([0, 50, 0, 0.15])
pp.savefig()
pp.close()
