#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Custwritecsv."""
import csv

with open("write.csv", "wt", encoding="utf-8") as f:
    csv_writer = csv.writer(f, delimiter="\t", lineterminator="\n\n")
    csv_writer.writerow(["abc", "pqr", "xyz"])
    csv_writer.writerow(["123", "456", "789"])
