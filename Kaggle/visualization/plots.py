#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd

pd.set_option("display.max_rows", 5)
pd.set_option("display.max_columns", 6)
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages

pp = PdfPages("plots.pdf")
print("Setup Complete")

penguins = sns.load_dataset("penguins")
print(penguins.head())
plot = sns.histplot(data=penguins, x="flipper_length_mm", hue="species", multiple="stack")
plot.set_title("Fig 1: Histogram")
pp.savefig()
plot.figure.clear()

plot = sns.kdeplot(data=penguins, x="flipper_length_mm", hue="species", multiple="stack")
plot.set_title("Fig 2: KDE")
pp.savefig()
plot.figure.clear()

plot = sns.displot(data=penguins, x="flipper_length_mm", hue="species", multiple="stack")
plot.figure.suptitle("Fig 3: Displot stacked histogram")
pp.savefig()
plot.figure.clear()

plot = sns.displot(
    data=penguins, x="flipper_length_mm", hue="species", multiple="stack", kind="kde"
)
plot.figure.suptitle("Fig 4: Displot KDE")
pp.savefig()
plot.figure.clear()

plot = sns.displot(data=penguins, x="flipper_length_mm", hue="species", col="species")
plot.figure.suptitle("")
pp.savefig()
plot.figure.clear()

f, axs = plt.subplots(1, 2, figsize=(8, 4), gridspec_kw=dict(width_ratios=[4, 3]))
sns.scatterplot(data=penguins, x="flipper_length_mm", y="bill_length_mm", hue="species", ax=axs[0])
sns.histplot(
    data=penguins, x="species", hue="species", shrink=0.8, alpha=0.8, legend=False, ax=axs[1]
)
f.tight_layout()
pp.savefig()
f.figure.clear()

tips = sns.load_dataset("tips")
g = sns.relplot(data=tips, x="total_bill", y="tip")
g.ax.axline(xy1=(10, 2), slope=0.2, color="b", dashes=(5, 2))
pp.savefig()
g.figure.clear()

g = sns.relplot(data=penguins, x="flipper_length_mm", y="bill_length_mm", col="sex")
g.set_axis_labels("Flipper length (mm)", "Bill length (mm)")
pp.savefig()
g.figure.clear()

sns.jointplot(data=penguins, x="flipper_length_mm", y="bill_length_mm", hue="species")
pp.savefig()

sns.pairplot(data=penguins, hue="species")
pp.savefig()

sns.jointplot(data=penguins, x="flipper_length_mm", y="bill_length_mm", hue="species", kind="hist")
pp.savefig()

pp.close()
