#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
pd.set_option("display.max_rows", 5)
pd.set_option("display.max_columns", 6)
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('dists.pdf')
print("Setup Complete")


penguins = sns.load_dataset("penguins")
plot = sns.displot(data=penguins, x="flipper_length_mm")
plot.figure.suptitle("Fig 1")
pp.savefig()
plot.figure.clear()

pp.close()
