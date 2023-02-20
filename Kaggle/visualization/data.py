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

pp = PdfPages("data.pdf")
print("Setup Complete")

flights = sns.load_dataset("flights")
print(flights.head())

plot = sns.relplot(data=flights, x="year", y="passengers", hue="month", kind="line")
pp.savefig()
plot.figure.clear()

flights_wide = flights.pivot(index="year", columns="month", values="passengers")
print(flights_wide.head())
plot = sns.relplot(data=flights_wide, kind="line")
pp.savefig()
plot.figure.clear()

plot = sns.relplot(data=flights, x="month", y="passengers", hue="year", kind="line")
pp.savefig()
plot.figure.clear()

plot = sns.relplot(data=flights_wide.transpose(), kind="line")
pp.savefig()
plot.figure.clear()

plot = sns.catplot(data=flights_wide, kind="box")
pp.savefig()
plot.figure.clear()

anagrams = sns.load_dataset("anagrams")
print(anagrams)

anagrams_long = anagrams.melt(
    id_vars=["subidr", "attnr"], var_name="solutions", value_name="score"
)
print(anagrams_long.head())

plot = sns.catplot(data=anagrams_long, x="solutions", y="score", hue="attnr", kind="point")
pp.savefig()
plot.figure.clear()

pp.close()
