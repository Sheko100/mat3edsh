#!/usr/bin/python3
"""Module that strips the duplicated pages of a PDF document
    
    This module is using PyPDF2 package to strip the duplicated pages which are two
    pages that are identical and next to each other
"""
import sys
from PyPDF2 import PdfReader, PdfWriter

if len(sys.argv) != 2:
    print("Usage: ./mat3edsh <pdf_file_path>", file=sys.stderr)
    sys.exit(1)

pdfpath = sys.argv[1]
try:
    pdfdoc = PdfReader(pdfpath);
except FileNotFoundError:
    print("file '{}' not found".format(pdfpath), file=sys.stderr)
    sys.exit(1)

pen = PdfWriter()
pagenum = 0
output = "{}_new.pdf".format(pdfpath[:-4])

for page in pdfdoc.pages:
    if pagenum % 2 != 0:
        pen.add_page(page)
    pagenum += 1

pen.add_metadata(pdfdoc.metadata)

with open(output, mode="wb") as newpdf:
    pen.write(newpdf)
