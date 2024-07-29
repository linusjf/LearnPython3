#!/usr/bin/env python
"""
Food Delivery Costs Analysis.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : fdca.py
# @created     : Sunday Jul 28, 2024 19:17:13 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

pd.set_option('display.max_columns', None)

pp = PdfPages("fdca.pdf")
print("Setup Complete")

df = pd.read_csv("food delivery costs.csv")

print(df)

# cleaning our data
df["Order Date and Time"] = pd.to_datetime(df["Order Date and Time"])
df["Delivery Date and Time"] = pd.to_datetime(df["Delivery Date and Time"])


def extract(value):
    """ Extract"""
    arr = str(value).split(" ")
    val = removepctsymbol(arr[0])
    return val


def removepctsymbol(value):
    """ Remove pct symbol"""
    if "%" in value:
        val = value.replace("%", "")
        return float(val)
    return float(value)


df["Discounts and Offers"] = df["Discounts and Offers"].apply(extract)
df.loc[df["Discounts and Offers"] <= 15, "Discounts and Offers"] = df[
    "Discounts and Offers"] / 100 * df["Order Value"]
df["Discounts and Offers"] = df["Discounts and Offers"].fillna(0)
df = df.rename(columns={"Commission Fee": "Commissions"})

df["Costs"] = df["Delivery Fee"] + df['Discounts and Offers'] + df[
    "Payment Processing Fee"]

df["Profit"] = df["Commissions"] - df['Costs']
print(df["Profit"].sum())

cost_dist = df[[
    "Delivery Fee", "Payment Processing Fee", "Discounts and Offers"
]].sum()
print(cost_dist)

print(df.info())
print(df.head())

plt.pie(cost_dist, labels=cost_dist.index, autopct="%1.2f%%")
pp.savefig()
plt.clf()

abc = df[["Commissions", "Costs", "Profit"]].sum()
print(abc)

plt.bar(abc.index, abc)
# plt.xticks(rotation=90)
pp.savefig()
plt.clf()

plt.hist(df["Profit"])

pp.savefig()
pp.close()
