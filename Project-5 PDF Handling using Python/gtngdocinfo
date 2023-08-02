#Python program to get PDF info using PyPDF2 Library
from PyPDF2 import PdfFileReader

pdf_name="D:\COMICS\NINJAS\PDFs\Antony Cummins' and Yoshie Minami's 'The Secret Traditions of the Shinobi (Hattori Hanzo's Shinobi Hiden and Other Ninja Scrolls)'.pdf"
f = open(pdf_name,'rb')
pdf = PdfFileReader(f)
information = pdf.getDocumentInfo()
print(information)
f.close()
