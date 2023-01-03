#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xlsxwriter
workbook = xlsxwriter.Workbook('chartcolumn.xlsx')
worksheet = workbook.add_worksheet()
chart = workbook.add_chart({'type': 'column'})
data = [
 ['Year', '2013', '2014', '2015'],
 ['Revenue', 100, 120, 125],
 ['COGS', 80, 90, 70],
 ['Profit', 20, 30, 55],
 ]
worksheet.write_row('A1', data[0])
worksheet.write_row('A2', data[1])
worksheet.write_row('A3', data[2])
worksheet.write_row('A4', data[3])
chart.add_series({'values': '=Sheet1!$B$2:$B$4', 'name':'2013'})
chart.add_series({'values': '=Sheet1!$C$2:$C$4', 'name':'2014'})
chart.add_series({'values': '=Sheet1!$D$2:$D$4', 'name':'2015'})
worksheet.insert_chart('G1', chart)
worksheet.write(5, 0, '% Gain')
worksheet.write(5, 1, '=(B4/B2)*100')
worksheet.write(5, 2, '=(C4/C2)*100')
worksheet.write(5, 3, '=(D4/D2)*100')
workbook.close()
