#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

pp = PdfPages("random_walk.pdf")
print("Setup Complete")

# number of walkers
n_stories = 1000
# time during which we follow the walker
t_max = 200
t = np.arange(t_max)
# +1 because the high value is exclusive
steps = 2 * np.random.randint(0, 1 + 1, (n_stories, t_max)) - 1
# Verification: all steps are 1 or -1
np.unique(steps)
# axis = 1: dimension of time
positions = np.cumsum(steps, axis=1)
sq_distance = positions**2
mean_sq_distance = np.mean(sq_distance, axis=0)
print(np.isclose(np.sqrt(mean_sq_distance), np.sqrt(t), atol=1.0).all())
print(np.isclose(np.sqrt(mean_sq_distance), np.sqrt(t), atol=0.5).all())
plt.figure(figsize=(4, 3))
plt.plot(t, np.sqrt(mean_sq_distance), "g.", t, np.sqrt(t), "y-")
plt.xlabel(r"$t$")
plt.ylabel(r"$\sqrt{\langle (\delta x)^2 \rangle}$")
# provide sufficient space for labels
plt.tight_layout()
pp.savefig()
plt.clf()

pp.close()
