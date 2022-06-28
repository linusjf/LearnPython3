#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sklearn.datasets import load_sample_image
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import numpy as np

# The PDF document
pdf_pages = PdfPages("flowerkmeans.pdf")

china = load_sample_image("flower.jpg")
ax = plt.axes(xticks=[],yticks=[])
ax.imshow(china)
pdf_pages.savefig()
pdf_pages.close()

print(china.shape)

data = china / 255.0
data = data.reshape(427 * 640, 3)
print(data.shape)

