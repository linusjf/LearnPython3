#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)

print(reviews.groupby('points').points.count())

print(reviews.groupby('points').price.min())

print(reviews.groupby('winery').apply(lambda df: df.title.iloc[0]))

print(reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()]))

print(reviews.groupby(['country']).price.agg([len, min, max]))
