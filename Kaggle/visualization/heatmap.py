#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

np.random.seed(0)
import pandas as pd

pd.set_option("display.max_rows", 5)
pd.set_option("display.max_columns", 6)
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()
from matplotlib.backends.backend_pdf import PdfPages

pp = PdfPages("heatmap.pdf")
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

normal_data = np.random.randn(10, 12)
ax = sns.heatmap(normal_data, center=0)
ax.set_title("Fig 3")
pp.savefig()
ax.get_figure().clf()

flights = sns.load_dataset("flights")
flights = flights.pivot("month", "year", "passengers")
ax = sns.heatmap(flights)
ax.set_title("Flights 1")
pp.savefig()
ax.get_figure().clf()

ax = sns.heatmap(flights, annot=True, fmt="d")
ax.set_title("Flights (Annotated)")
pp.savefig()
ax.get_figure().clf()

ax = sns.heatmap(flights, linewidths=0.5)
ax.set_title("Flights (Lines)")
pp.savefig()
ax.get_figure().clf()

ax = sns.heatmap(flights, cmap="YlGnBu")
ax.set_title("Flights (ColorMap)")
pp.savefig()
ax.get_figure().clf()

ax = sns.heatmap(flights, center=flights.loc["Jan", 1955])
ax.set_title("Flights (Centered)")
pp.savefig()
ax.get_figure().clf()

data = np.random.randn(50, 20)
ax = sns.heatmap(data, xticklabels=2, yticklabels=False)
ax.set_title("Flights (Alternate)")
pp.savefig()
ax.get_figure().clf()

ax = sns.heatmap(flights, cbar=False)
ax.set_title("Flights (No ColorBar)")
pp.savefig()
ax.get_figure().clf()

grid_kws = {"height_ratios": (0.9, 0.05), "hspace": 0.3}
f, (ax, cbar_ax) = plt.subplots(2, gridspec_kw=grid_kws)
ax = sns.heatmap(flights, ax=ax, cbar_ax=cbar_ax, cbar_kws={"orientation": "horizontal"})
ax.set_title("Flights (Different Axes)")
pp.savefig()
ax.get_figure().clf()

corr = np.corrcoef(np.random.randn(10, 200))
mask = np.zeros_like(corr)
mask[np.triu_indices_from(mask)] = True
with sns.axes_style("white"):
    f, ax = plt.subplots(figsize=(7, 5))
    ax = sns.heatmap(corr, mask=mask, vmax=0.3, square=True)
    ax.set_title("Flights (Mask)")
    pp.savefig()
    ax.get_figure().clf()

pp.close()
