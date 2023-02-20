#!/usr/bin/env python
# -*- coding: utf-8 -*-
import PyPDF2
from PyPDF2 import PdfReader

pdf = open("diveintopython.pdf", "rb")
readerObj = PdfReader(pdf, strict=False)
print("PDF Reader Object is:", readerObj)
print("Details of diveintopython book")
print("Number of pages:", len(readerObj.pages))
print("Title:", readerObj.metadata.title)
print("Author:", readerObj.metadata.author)

print("Reading Page 1")
page = readerObj.pages[0]
print(page.extract_text())

print("Book Outline")
for heading in readerObj.outline:
    if type(heading) is not list:
        print(dict(heading).get("/Title"))
