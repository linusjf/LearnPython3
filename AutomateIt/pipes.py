#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv

print("Available dialects: ", csv.list_dialects())
for dialect in csv.list_dialects():
    d = csv.get_dialect(dialect)
    print("Dialect: ", dialect)
    print("--------------")
    print("Delimiter: ", d.delimiter)
    print("Doublequote: ", d.doublequote)
    print("Escapechar: ", d.escapechar)
    print("lineterminator: ", repr(d.lineterminator))
    print("quotechar: ", d.quotechar)
    print("Quoting: ", d.quoting)
    print("skipinitialspace: ", d.skipinitialspace)
    print("strict: ", d.strict)
    print()
csv.register_dialect("pipes", delimiter="-")
with open("pipes.csv", "r") as f:
    reader = csv.reader(f, dialect="pipes")
    for row in reader:
        print(row)
