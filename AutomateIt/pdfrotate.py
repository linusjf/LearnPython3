#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyPDF2 import PdfReader, PdfWriter
fp = open('diveintopython.pdf', 'rb')
readerObj = PdfReader(fp)
page = readerObj.pages[0]
page.rotate(90)
writer = PdfWriter()
writer.add_page(page)
fw = open('rotated.pdf', 'wb')
writer.write(fw)
fw.close()
fp.close()
