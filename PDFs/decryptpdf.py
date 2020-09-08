import PyPDF2,sys,time,getpass
from tqdm import tqdm
pdfname = input("Input the name of the pdf you want to decrypt (Example: hello.pdf): ")
pdfname =pdfname.strip()
if pdfname.endswith(".pdf") == False:
    print("Enter a proper pdf name")
    print("Shutting down program...")
    time.sleep(5)
    sys.exit(0)
pdfReader = PyPDF2.PdfFileReader(open(pdfname, 'rb'))
if pdfReader.isEncrypted:
    print("Input the password for decrypting the file")
    p = getpass.getpass()
    print("DECRYPTING...")
    for i in tqdm(range(2)):
        time.sleep(3)
    pdfReader.decrypt(p)
    print("DONE!")
#pageObj = pdfReader.getPage(0)