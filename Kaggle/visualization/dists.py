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

# Path of the file to read
iris_filepath = "iris.csv"

# Read the file into a variable iris_data
iris_data = pd.read_csv(iris_filepath, index_col="Id")

# Print the first 5 rows of the data
print(iris_data.head())

# Histogram 
plot = sns.histplot(iris_data, x='PetalLengthCm')
plot.set_title("Fig 1")
pp.savefig()
plot.figure.clear()

penguins = sns.load_dataset("penguins")
plot = sns.histplot(data=penguins, x="flipper_length_mm")
plot.set_title("Fig 2")
pp.savefig()
plot.figure.clear()

plot = sns.histplot(data=penguins, y="flipper_length_mm")
plot.set_title("Fig 3")
pp.savefig()
plot.figure.clear()

plot = sns.histplot(data=penguins, x="flipper_length_mm", binwidth=3)
plot.set_title("Fig 4")
pp.savefig()
plot.figure.clear()

plot = sns.histplot(data=penguins, x="flipper_length_mm", bins=30)
plot.set_title("Fig 5")
pp.savefig()
plot.figure.clear()

plot = sns.histplot(data=penguins, x="flipper_length_mm", kde=True)
plot.set_title("Fig 6")
pp.savefig()
plot.figure.clear()

plot = sns.histplot(data=penguins)
plot.set_title("Fig 7")
pp.savefig()
plot.figure.clear()

pp.close()
