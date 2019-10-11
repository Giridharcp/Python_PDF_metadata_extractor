import os
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfparser import PDFDocument

fp = open(r"C:\Users\Giridhar\Documents\Calibre Library\Amish Tripathi\Scion of Ikshvaku (Ram Chandra Seri (144)\Scion of Ikshvaku (Ram Chandra - Amish Tripathi.pdf", 'rb')
parser = PDFParser(fp)
doc = PDFDocument(parser)
parser.set_document(doc)
doc.set_parser(parser)
if len(doc.info) > 0:
    meta = doc.info[0]
    meta=str(meta)
    info=meta.replace('\'','').replace('{','').replace('}','')
    info=info.split(',')
    for i in info:
       print(i)
