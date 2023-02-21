#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""PDFRead."""
from PyPDF2 import PdfReader

with open("diveintopython.pdf", "rb", encoding="utf-8") as pdf:
    reader = PdfReader(pdf, strict=False)
    print("PDF Reader Object is:", reader)
    print("Details of diveintopython book")
    print("Number of pages:", len(reader.pages))
    print("Title:", reader.metadata.title)
    print("Author:", reader.metadata.author)

    print("Reading Page 1")
    page = reader.pages[0]
    print(page.extract_text())  # pylint: disable=no-member

    print("Book Outline")
for heading in reader.outline:
    if not isinstance(heading, list):
        print(dict(heading).get("/Title"))
