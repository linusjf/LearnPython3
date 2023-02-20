#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

pd.set_option("display.max_rows", 5)
pd.set_option("display.max_columns", 6)
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt

plt.rcParams.update({"figure.max_open_warning": 0})
import seaborn as sns

sns.set_theme(color_codes=True)
from matplotlib.backends.backend_pdf import PdfPages

pp = PdfPages("clustermaps.pdf")
print("Setup Complete")

iris = sns.load_dataset("iris")
print(iris.head())
species = iris.pop("species")
g = sns.clustermap(iris)
pp.savefig()
g.figure.clear()

g = sns.clustermap(
    iris,
    figsize=(7, 5),
    row_cluster=False,
    dendrogram_ratio=(0.1, 0.2),
    cbar_pos=(0, 0.2, 0.03, 0.4),
)
pp.savefig()
g.figure.clear()

lut = dict(zip(species.unique(), "rbg"))
row_colors = species.map(lut)
g = sns.clustermap(iris, row_colors=row_colors)
pp.savefig()
g.figure.clear()

g = sns.clustermap(iris, cmap="mako", vmin=0, vmax=10)
pp.savefig()
g.figure.clear()

g = sns.clustermap(iris, metric="correlation")
pp.savefig()
g.figure.clear()

g = sns.clustermap(iris, method="single")
pp.savefig()
g.figure.clear()

g = sns.clustermap(iris, standard_scale=1)
pp.savefig()
g.figure.clear()

g = sns.clustermap(iris, z_score=0, cmap="vlag")
pp.savefig()
g.figure.clear()

pp.close()
