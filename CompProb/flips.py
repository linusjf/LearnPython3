#!/usr/bin/env python
# -*- coding: utf-8 -*-
import comp_prob_inference as cpi
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt

# The PDF document
pdf_pages = PdfPages("flips.pdf")

print(cpi.flip_fair_coin())
flips = cpi.flip_fair_coins(100)

cpi.plot_discrete_histogram(flips)
pdf_pages.savefig()

cpi.plot_discrete_histogram(flips, frequency=True)
pdf_pages.savefig()

n = 100000
heads_so_far = 0
fraction_of_heads = []
for i in range(n):
    if cpi.flip_fair_coin() == "heads":
        heads_so_far += 1
    fraction_of_heads.append(heads_so_far / (i + 1))

plt.figure(figsize=(8, 4))
plt.plot(range(1, n + 1), fraction_of_heads)
plt.xlabel("Number of flips")
plt.ylabel("Fraction of heads")

pdf_pages.savefig()
pdf_pages.close()

prob_space = {"sunny": 1 / 2, "rainy": 1 / 6, "snowy": 1 / 3}
random_outcome = cpi.sample_from_finite_probability_space(prob_space)
W = random_outcome
if random_outcome == "sunny":
    I = 1
else:
    I = 0
print(I)
