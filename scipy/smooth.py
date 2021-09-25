#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1.5, 1.5, 101)

plt.plot(x, np.sqrt(.2 + x**2), linewidth=2)
plt.text(-1, 0, '$f$', size=20)

plt.text(-1, 0, '$f$', size=20)

plt.ylim(ymin=-.2)
plt.axis('off')
plt.tight_layout()
plt.savefig('smooth.png')
plt.clf()
# A non-smooth function
plt.plot(x, np.abs(x), linewidth=2)
plt.text(-1, 0, '$f$', size=20)

plt.ylim(ymin=-.2)
plt.axis('off')
plt.tight_layout()
plt.savefig("nonsmooth.png")
