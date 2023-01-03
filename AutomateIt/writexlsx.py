#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xlsxwriter
workbook = xlsxwriter.Workbook('addsheet.xlsx')
worksheet = workbook.add_worksheet(name='Sheets')
workbook.close()

workbook = xlsxwriter.Workbook('expenses.xlsx')
worksheet = workbook.add_worksheet()
expenses = (
 ['Rent', 1000],
 ['Gas', 100],
 ['Food', 300],
 ['Gym', 50],
 )
row = 0
col = 0
for item, cost in (expenses):
    worksheet.write(row, col, item)
    worksheet.write(row, col + 1, cost)
    row += 1
worksheet.write(row, 0, 'Total')
worksheet.write_formula('B5', '=SUM(B1:B4)')

cellformat = workbook.add_format({'bg_color': 'blue',
 'font_color': 'red'})
worksheet.conditional_format('B1:KB5',
 {'type': 'cell',
 'criteria': '>=',
 'value': 150,
 'format': cellformat}
 )
workbook.close()
