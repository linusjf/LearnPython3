#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np; 
np.random.seed(0)
import pandas as pd
pd.set_option("display.max_rows", 5)
pd.set_option("display.max_columns", 6)
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()
from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('heatmap.pdf')
print("Setup Complete")

uniform_data = np.random.rand(10, 12)

ax = sns.heatmap(uniform_data)
ax.set_title("Fig 1")
pp.savefig()
ax.get_figure().clf()

ax = sns.heatmap(uniform_data, vmin=0, vmax=1)
ax.set_title("Fig 2")
pp.savefig()
ax.get_figure().clf()

pp.close()
