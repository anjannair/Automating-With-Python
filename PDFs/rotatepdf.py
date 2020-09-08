import PyPDF2
from PyPDF2 import PdfFileWriter, PdfFileReader
import time,sys,os
pdfname = input("Enter the name of your file (example: Hello.pdf) :")
pdfname =pdfname.strip()
if pdfname.endswith(".pdf") == False:
    print("Enter a proper pdf name")
    print("Shutting down program...")
    time.sleep(5)
    sys.exit(0)
pdfget = open(pdfname, 'rb')
pdfWriter = PyPDF2.PdfFileWriter()
pdfReader = PyPDF2.PdfFileReader(pdfget)
page = input("Enter the page number to rotate: ")
newpage = pdfReader.getPage(int(page)-1)
for pageNum in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)
    pdfWriter.addPage(pageObj)
angle = input("What angle (90/270/180): ")
clock = input("Clockwise or AntiClockwise (c/ac): ")
if clock == "c":
    time.sleep(5)
    newpage.rotateClockwise(int(angle))
elif clock == "ac":
    time.sleep(5)
    newpage.rotateCounterClockwise(int(angle))
pdfWriter.addPage(newpage)
resultPdfFile = open('rotatedPage.pdf', 'wb')
pdfWriter.write(resultPdfFile)
resultPdfFile.close()
resultPdfFile1 = open('rotatedPage.pdf', 'rb')
pdfReader1 = PyPDF2.PdfFileReader(resultPdfFile1)
pageObj = pdfReader1.getPage(0)
pdfWriter.addPage(pageObj)
#if int(page) != pdfReader.numPages:
#    for pageNum in range(int(page)-1,pdfReader.numPages):
#        pageObj = pdfReader.getPage(pageNum)
#        pdfWriter.addPage(pageObj)
pdfOutputFile = open('combinedfile.pdf', 'wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
pdffinal = PdfFileReader('combinedfile.pdf', 'rb')
output = PdfFileWriter()

for i in range(pdffinal.getNumPages()-2):
    p = pdffinal.getPage(i)
    output.addPage(p)

with open('final.pdf', 'wb') as f:
    output.write(f)

print("DONE!")
resultPdfFile1.close()
pdfget.close()
os.remove("rotatedPage.pdf")
os.remove("combinedfile.pdf")