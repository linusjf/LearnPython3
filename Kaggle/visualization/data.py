#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
pd.set_option("display.max_rows", 5)
pd.set_option("display.max_columns", 6)
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()
from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('data.pdf')
print("Setup Complete")

flights = sns.load_dataset("flights")
print(flights.head())

plot = sns.relplot(data=flights, x="year", y="passengers", hue="month", kind="line")
plot.figure.suptitle("Fig 1")
pp.savefig()
plot.figure.clear()

pp.close()
