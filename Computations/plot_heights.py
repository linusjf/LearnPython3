#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import zeros
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

pp = PdfPages("plot_heights.pdf")
print("Setup Complete")

h = zeros(4)
h[0] = 1.60
h[1] = 1.85
h[2] = 1.75
h[3] = 1.80
hft = h * 3.281
H = zeros(4)
H[0] = 0.50
H[1] = 0.70
H[2] = 1.90
H[3] = 1.75
HFT = H * 3.281

family_member_no = zeros(4)
family_member_no[0] = 0
family_member_no[1] = 1
family_member_no[2] = 2
family_member_no[3] = 3

plt.plot(family_member_no, h, family_member_no, H)
plt.xlabel("Family member number")
plt.ylabel("Height (m)")
plt.show()
pp.savefig()
plt.clf()
plt.plot(family_member_no, hft, family_member_no, HFT)
plt.xlabel("Family member number")
plt.ylabel("Height (ft)")
plt.show()
pp.savefig()
pp.close()
