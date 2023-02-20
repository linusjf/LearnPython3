#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv

f = open("write.csv", "wt")
csvWriter = csv.writer(f, delimiter="\t", lineterminator="\n\n")
csvWriter.writerow(["abc", "pqr", "xyz"])
csvWriter.writerow(["123", "456", "789"])
f.close()
