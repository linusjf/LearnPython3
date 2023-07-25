#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""PDFRotate."""
from pypdf import PdfReader, PdfWriter

with open("diveintopython.pdf", "rb") as fp:
    reader = PdfReader(fp)
    PAGE = reader.pages[0]
    PAGE.rotate(90)
    writer = PdfWriter()
    writer.add_page(PAGE)
    with open("rotated.pdf", "wb") as fw:
        writer.write(fw)
