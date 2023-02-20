#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""ReadCSV."""
import csv

with open("mylist.csv", "rt", encoding="utf-8") as fh:
    reader = csv.reader(fh)
    print("Data from the CSV:")
    print(list(reader))
