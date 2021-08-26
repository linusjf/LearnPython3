#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
pd.set_option("display.max_rows", 5)
pd.set_option("display.max_columns", 6)
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('kde.pdf')
print("Setup Complete")

tips = sns.load_dataset("tips")
plot = sns.kdeplot(data=tips, x="total_bill")
plot.set_title("Fig 1")
pp.savefig()
plot.figure.clear()


pp.close()
