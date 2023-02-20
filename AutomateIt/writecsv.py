#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""WriteCSV."""
import csv

names = ["John", "Eve", "Fate", "Jadon"]
grades = ["C", "A+", "A", "B-"]
with open("newlist.csv", "wt", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(("Sr.", "Names", "Grades"))
    for i in range(4):
        writer.writerow((i + 1, names[i], grades[i]))
