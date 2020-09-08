# Design a word document with your watermark and save it as 
# watermark.pdf in the same folder
import PyPDF2,sys,time,os
from tqdm import tqdm
from PyPDF2 import PdfFileWriter, PdfFileReader
pdfname = input("Input the name of the pdf you want to watermark (Example: hello.pdf): ")
pdfname =pdfname.strip()
if pdfname.endswith(".pdf") == False:
    print("Enter a proper pdf name")
    print("Shutting down program...")
    time.sleep(5)
    sys.exit(0)
waterfile = open(pdfname, 'rb')
pdfReader = PyPDF2.PdfFileReader(waterfile)
inp = input("Watermark one or all pages? (o/a): ")
if inp =="o":
    page = input("Which page number? :")
    waterpage = pdfReader.getPage(int(page)-1)
    pdfWatermarkReader = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb'))
    waterpage.mergePage(pdfWatermarkReader.getPage(0))
    pdfWriter = PyPDF2.PdfFileWriter()
    pdfWriter.addPage(waterpage)
    for pageNum in range(0, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
    resultPdfFile = open('watermarked.pdf', 'wb')
    pdfWriter.write(resultPdfFile)
    resultPdfFile.close()
    pdffinal = PdfFileReader('watermarked.pdf', 'rb')
    output = PdfFileWriter()
    for i in range(1,pdffinal.numPages):
        p = pdffinal.getPage(i)
        output.addPage(p)

    with open('finalwatermark.pdf', 'wb') as f:
        output.write(f)
    print("WATERMARKING...")
    for i in tqdm(range(5)):
        time.sleep(3)
    print("DONE!")
    waterfile.close()
    os.remove("watermarked.pdf")
elif inp=="a":
    output = PdfFileWriter()
    for i in range(0,pdfReader.numPages):
        waterpage = pdfReader.getPage(i)
        pdfWatermarkReader = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb'))
        waterpage.mergePage(pdfWatermarkReader.getPage(0))
        pdfWriter = PyPDF2.PdfFileWriter()
        pdfWriter.addPage(waterpage)
        output.addPage(waterpage)
    with open('finalwatermark.pdf', 'wb') as f:
        output.write(f)
    print("WATERMARKING...")
    for i in tqdm(range(5)):
        time.sleep(3)
    print("DONE!")