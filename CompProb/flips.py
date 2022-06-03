#!/usr/bin/env python
# -*- coding: utf-8 -*-
import comp_prob_inference as cpi
from matplotlib.backends.backend_pdf import PdfPages

# The PDF document
pdf_pages = PdfPages("flips.pdf")

print(cpi.flip_fair_coin())
flips = cpi.flip_fair_coins(100)

cpi.plot_discrete_histogram(flips)
pdf_pages.savefig()

cpi.plot_discrete_histogram(flips, frequency=True)
pdf_pages.savefig()
pdf_pages.close()
