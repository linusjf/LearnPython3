#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
pd.set_option("display.max_rows", 5)
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('lineplot.pdf')
print("Setup Complete")

flights = sns.load_dataset("flights")
print(flights.head())

may_flights = flights.query("month == 'May'")
sns.lineplot(data=may_flights, x="year", y="passengers")
pp.savefig()

flights_wide = flights.pivot("year", "month", "passengers")
print(flights_wide.head())

sns.lineplot(data=flights_wide["May"])
pp.savefig()

sns.lineplot(data=flights_wide)
pp.savefig()

sns.lineplot(data=flights, x="year", y="passengers")
pp.savefig()

sns.lineplot(data=flights, x="year", y="passengers", hue="month")
pp.savefig()

sns.lineplot(data=flights, x="year", y="passengers", hue="month", style="month")
pp.savefig()

pp.close()
