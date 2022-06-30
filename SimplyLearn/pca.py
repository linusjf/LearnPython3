#!/usr/bin/env python
# -*- coding: utf-8 -*-
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

# The PDF document
pdf_pages = PdfPages("pca.pdf")

pdf_pages.savefig()
pdf_pages.close()
