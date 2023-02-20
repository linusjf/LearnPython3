#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd

pd.set_option("display.max_rows", None)
pd.set_option("display.max_rows", None)
# Read the data
data = pd.read_csv("AER_credit_card_data.csv", true_values=["yes"], false_values=["no"])

# Select target
y = data.card

# Select predictors
X = data.drop(["card"], axis=1)

print("Number of rows in the dataset:", X.shape[0])
# more options can be specified also
with pd.option_context("display.max_rows", None, "display.max_columns", None):
    print(X.head())

from sklearn.pipeline import make_pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

# Since there is no preprocessing, we don't need a pipeline (used anyway as best practice!)
my_pipeline = make_pipeline(RandomForestClassifier(n_estimators=100))
cv_scores = cross_val_score(my_pipeline, X, y, cv=5, scoring="accuracy")

print("Cross-validation accuracy: %f" % cv_scores.mean())

expenditures_cardholders = X.expenditure[y]
expenditures_noncardholders = X.expenditure[~y]

print(
    "Fraction of those who did not receive a card and had no expenditures: %.2f"
    % ((expenditures_noncardholders == 0).mean())
)
print(
    "Fraction of those who received a card and had no expenditures: %.2f"
    % ((expenditures_cardholders == 0).mean())
)

# Drop leaky predictors from dataset
potential_leaks = ["expenditure", "share", "active", "majorcards"]
X2 = X.drop(potential_leaks, axis=1)

# Evaluate the model with leaky predictors removed
cv_scores = cross_val_score(my_pipeline, X2, y, cv=5, scoring="accuracy")

print("Cross-val accuracy: %f" % cv_scores.mean())
