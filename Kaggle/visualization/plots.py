#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
pd.set_option("display.max_rows", 5)
pd.set_option("display.max_columns", 6)
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('plots.pdf')
print("Setup Complete")

penguins = sns.load_dataset("penguins")
print(penguins.head())
plot = sns.histplot(data=penguins, x="flipper_length_mm", hue="species", multiple="stack")
plot.set_title("Fig 1: Histogram")
pp.savefig()
plot.figure.clear()

pp.close()
