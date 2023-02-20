#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd

pd.set_option("display.max_rows", 500)
pd.set_option("display.max_columns", 500)
pd.set_option("display.width", 1000)
import numpy as np

reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)
print(reviews.head())
print(reviews.points.describe())
print(reviews.points.mean())
print(reviews.taster_name.describe())
print(reviews.taster_name.unique())
print(reviews.taster_name.value_counts())
review_points_mean = reviews.points.mean()
print(reviews.points.map(lambda p: p - review_points_mean).head())
print(reviews.points.map(lambda p: p - review_points_mean).tail())


def remean_points(row):
    row.points = row.points - review_points_mean
    return row


print(reviews.head().apply(remean_points, axis="columns").points)
print(reviews.tail().apply(remean_points, axis="columns").points)
print(reviews.head(1))
review_points_mean = reviews.points.mean()
print((reviews.points - review_points_mean).head())
print((reviews.points - review_points_mean).tail())
print((reviews.country + " - " + reviews.region_1).head())
print((reviews.country + " - " + reviews.region_1).tail())
