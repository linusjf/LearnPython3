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
