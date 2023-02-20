#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""CAEmployees"""
import csv

with open("mylist.csv", "rt", encoding="utf-8") as f:
    with open("CAEmployees.csv", "wt", encoding="utf-8") as fw:
        reader = csv.DictReader(f)
        csv_writer = csv.writer(fw)
        for row in reader:
            if reader.line_num == 1:
                continue
            if row["state"] == "CA":
                csv_writer.writerow([row["email"], row["phone"]])
