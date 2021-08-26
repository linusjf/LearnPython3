#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
pd.set_option("display.max_rows", 5)
pd.set_option("display.max_columns", 6)
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('ecdf.pdf')
print("Setup Complete")

penguins = sns.load_dataset("penguins")
print(penguins.head())
plot = sns.ecdfplot(data=penguins, x="flipper_length_mm")
plot.set_title("Penguins flipper length")
pp.savefig()
plot.figure.clear()

plot = sns.ecdfplot(data=penguins, y="flipper_length_mm")
plot.set_title("Penguins flipper length (y-axis)")
pp.savefig()
plot.figure.clear()

plot = sns.ecdfplot(data=penguins.filter(like="bill_", axis="columns"))
plot.set_title("Penguins bill%")
pp.savefig()
plot.figure.clear()

plot = sns.ecdfplot(data=penguins, x="bill_length_mm", hue="species")
plot.set_title("Penguins bill length per species")
pp.savefig()
plot.figure.clear()

plot = sns.ecdfplot(data=penguins, x="bill_length_mm", hue="species", stat="count")
plot.set_title("Penguins bill length (count)")
pp.savefig()
plot.figure.clear()

plot = sns.ecdfplot(data=penguins, x="bill_length_mm", hue="species", complementary=True)
plot.set_title("Penguins bill length (complementary)")
pp.savefig()
plot.figure.clear()
pp.close()
