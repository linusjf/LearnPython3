#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xlsxwriter
workbook = xlsxwriter.Workbook('addsheet.xlsx')
worksheet = workbook.add_worksheet(name='New Sheet 2')
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
worksheet.write(row, 1, '=SUM(B1:B4)')
workbook.close()
