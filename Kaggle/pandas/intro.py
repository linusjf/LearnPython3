#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd

pd.set_option("display.max_rows", 500)
pd.set_option("display.max_columns", 500)
pd.set_option("display.width", 1000)

df = pd.DataFrame({"Yes": [50, 21], "No": [131, 2]})
print(df)
df = pd.DataFrame({"Bob": ["I liked it.", "It was awful."], "Sue": ["Pretty good.", "Bland."]})
print(df)
df = pd.DataFrame(
    {"Bob": ["I liked it.", "It was awful."], "Sue": ["Pretty good.", "Bland."]},
    index=["Product A", "Product B"],
)
print(df)

df = pd.Series([1, 2, 3, 4, 5])
print(df)

df = pd.Series([30, 35, 40], index=["2015 Sales", "2016 Sales", "2017 Sales"], name="Product A")
print(df)

wine_reviews = pd.read_csv("winemag-data-130k-v2.csv")
print(wine_reviews.shape)
print(wine_reviews.head())

wine_reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)
print(wine_reviews.head())
