#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyPDF2 import PdfWriter, PdfReader

fp = open("diveintopython.pdf", "rb")
readerObj = PdfReader(fp)
writer = PdfWriter()
for page in range(len(readerObj.pages)):
    writer.add_page(readerObj.pages[page])
writer.encrypt("P@$$w0rd")
newfp = open("EncryptExercise.pdf", "wb")
writer.write(newfp)
newfp.close()
fp.close()
