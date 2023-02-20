#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Chartxlsx."""
import xlsxwriter

workbook = xlsxwriter.Workbook("chartline.xlsx")
worksheet = workbook.add_worksheet()
data = [10, 40, 50, 20, 10, 50]
worksheet.write_column("A1", data)
chart = workbook.add_chart({"type": "line"})
chart.add_series({"values": "=Sheet1!$A$1:$A$6"})
worksheet.insert_chart("C1", chart)
workbook.close()
