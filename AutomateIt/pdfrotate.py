#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""PDFRotate."""
from PyPDF2 import PdfReader, PdfWriter

with open("diveintopython.pdf", "rb", encoding="utf-8") as fp:
    reader = PdfReader(fp)
    page = reader.pages[0]
    page.rotate(90)  # pylint: disable=no-member
    writer = PdfWriter()
    writer.add_page(page)
    with open("rotated.pdf", "wb", encoding="utf-8") as fw:
        writer.write(fw)
