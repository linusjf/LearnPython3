#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""PDFRead."""
from pypdf import PdfReader

with open("diveintopython.pdf", "rb") as pdf:
    reader = PdfReader(pdf, strict=False)
    print("PDF Reader Object is:", reader)
    print("Details of diveintopython book")
    print("Number of pages:", len(reader.pages))
    if reader.metadata:
        print("Title:", reader.metadata.title)
        print("Author:", reader.metadata.author)

    print("Reading Page 1")
    PAGE = reader.pages[0]
    print(PAGE.extract_text())

    print("Book Outline")
    for heading in reader.outline:
        if not isinstance(heading, list):
            print(dict(heading).get("/Title"))
