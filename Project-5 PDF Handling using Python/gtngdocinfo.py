#Python program to get PDF info using PyPDF2 Library
from PyPDF2 import PdfFileReader

var="Y"
while(var=="y" or var=="Y"):
  pdf_name=input("Enter file name along with its path: ")
  f = open(pdf_name,'rb')
  pdf = PdfFileReader(f)
  information = pdf.getDocumentInfo()
  print(information)
  var= input("Press Y or y to get info of another pdf or press any other key to quit.")
f.close()
