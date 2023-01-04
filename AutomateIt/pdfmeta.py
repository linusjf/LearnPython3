#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyPDF2 import PdfMerger, PdfReader
mergerObj = PdfMerger()
fp = open('myPdf.pdf', 'wb')
metadata = {u'/edited':u'ByPdfMerger',}
mergerObj.add_metadata(metadata)
mergerObj.write(fp)
fp.close()
pdf = open("myPdf.pdf", 'rb')
readerObj = PdfReader(pdf)
print("Document Info:", readerObj.metadata)
pdf.close()
