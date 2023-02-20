#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd

reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)
pd.set_option("max_rows", 14)

print(reviews.price.dtype)
print(reviews.dtypes)

print(reviews.points.astype("float64"))

print(reviews.index.dtype)

print(reviews[pd.isnull(reviews.country)])

print(reviews.region_2.fillna("Unknown"))

print(reviews.taster_twitter_handle.replace("@kerinokeefe", "@kerino"))
