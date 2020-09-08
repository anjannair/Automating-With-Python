import PyPDF2
import sys
import time
pdfname = input("Enter the name of your file (example: Hello.pdf) :")
pdfname =pdfname.strip()
if pdfname.endswith(".pdf") == False:
    print("Enter a proper pdf name")
    print("Shutting down program...")
    time.sleep(5)
    sys.exit(0)
pdfFileObj = open(pdfname, 'rb') #If you get FileNotFoundError check if the file name you mentioned is in the same folder/directory
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print("Number of pages: "+ str(pdfReader.numPages))
while True:
    ans = input("Do you want to extract from one page or all (o/a) :")
    if ans=="o":
        page = input("Which page number? :")
        pageObj = pdfReader.getPage(int(page)-1)
        print("Extracting text......")
        time.sleep(5)
        with open("extractedtext.txt","a") as f:
            f.write(pageObj.extractText() + "\n")
        print("DONE!")
        break
    elif ans=="a":
        print("Extracting text......")
        for x in range(0,pdfReader.numPages):
            pageObj = pdfReader.getPage(x)
            with open("extractedtext.txt","a") as f:
                f.write(pageObj.extractText() + "\n")
        time.sleep(5)
        print("DONE!")
        break
pdfFileObj.close()