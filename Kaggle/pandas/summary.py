#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
import numpy as np
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)
print(reviews.head())
