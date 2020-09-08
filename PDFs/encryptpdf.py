import PyPDF2
import sys,time,getpass
from tqdm import tqdm
pdfname = input("Input the name of the pdf you want to encrypt (Example: hello.pdf): ")
pdfname =pdfname.strip()
if pdfname.endswith(".pdf") == False:
    print("Enter a proper pdf name")
    print("Shutting down program...")
    time.sleep(5)
    sys.exit(0)
print("Input the password you want to use for the encryption below")
passw = getpass.getpass()
pdfFile = open(pdfname, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
pdfWriter = PyPDF2.PdfFileWriter()
for pageNum in range(pdfReader.numPages):
    pdfWriter.addPage(pdfReader.getPage(pageNum))
pdfWriter.encrypt(passw)
resultPdf = open('encryptedfile.pdf', 'wb')
pdfWriter.write(resultPdf)
print("ENCRYPTING...")
for i in tqdm(range(5)):
    time.sleep(3)
print("DONE!")
resultPdf.close()