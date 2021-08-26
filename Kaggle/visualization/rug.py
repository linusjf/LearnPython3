#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
pd.set_option("display.max_rows", 5)
pd.set_option("display.max_columns", 6)
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()
from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('rug.pdf')
print("Setup Complete")

tips = sns.load_dataset("tips")
print(tips.head())
plot = sns.kdeplot(data=tips, x="total_bill")
sns.rugplot(data=tips, x="total_bill")
plot.set_title("Tips rug plot X-axis")
pp.savefig()
plot.figure.clear()

plot = sns.scatterplot(data=tips, x="total_bill", y="tip")
sns.rugplot(data=tips, x="total_bill", y="tip")
plot.set_title("Tips rug plot (both axes)")
pp.savefig()
plot.figure.clear()

plot = sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time")
sns.rugplot(data=tips, x="total_bill", y="tip", hue="time")
plot.set_title("Tips rug plot with hues")
pp.savefig()
plot.figure.clear()

plot = sns.scatterplot(data=tips, x="total_bill", y="tip")
sns.rugplot(data=tips, x="total_bill", y="tip", height=.1)
plot.set_title("Tips taller rug plot")
pp.savefig()
plot.figure.clear()

plot = sns.scatterplot(data=tips, x="total_bill", y="tip")
sns.rugplot(data=tips, x="total_bill", y="tip", height=-.02, clip_on=False)
plot.set_title("Tips rug outside axes plot")
pp.savefig()
plot.figure.clear()

diamonds = sns.load_dataset("diamonds")
print(diamonds.head())
plot = sns.scatterplot(data=diamonds, x="carat", y="price", s=5)
sns.rugplot(data=diamonds, x="carat", y="price", lw=1, alpha=.005)
plot.set_title("Diamonds rug carat price")
pp.savefig()
plot.figure.clear()

pp.close()
