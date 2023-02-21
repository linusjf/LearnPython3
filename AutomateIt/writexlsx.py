#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""WriteXLSX."""
import xlsxwriter  # type: ignore

workbook = xlsxwriter.Workbook("addsheet.xlsx")
worksheet = workbook.add_worksheet(name="Sheets")
workbook.close()

workbook = xlsxwriter.Workbook("expenses.xlsx")
worksheet = workbook.add_worksheet()
expenses = (
    ["Rent", 1000],
    ["Gas", 100],
    ["Food", 300],
    ["Gym", 50],
)
ROW = 0
COL = 0
for item, cost in expenses:
    worksheet.write(ROW, COL, item)
    worksheet.write(ROW, COL + 1, cost)
    ROW += 1
worksheet.write(ROW, 0, "Total")
worksheet.write_formula("B5", "=SUM(B1:B4)")

cellformat = workbook.add_format({"bg_color": "blue", "font_color": "red"})
worksheet.conditional_format(
    "B1:KB5", {"type": "cell", "criteria": ">=", "value": 150, "format": cellformat}
)
workbook.close()
