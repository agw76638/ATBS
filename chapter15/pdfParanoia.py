import PyPDF2, os, sys

def encryptPdf(folder):
    folder = os.path.abspath(folder)
    # Go through folder.
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            # Encrypt PDF using a password provided on the command line.
            if filename.endswith('.pdf'):
                pdfFile = open(os.path.join(foldername, filename), 'rb')
                pdfReader = PyPDF2.PdfFileReader(pdfFile)
                pdfWriter = PyPDF2.PdfFileWriter()
                pdfWriter.encrypt(password)

                # Save encrypted PDF with an _encrypted.pdf suffix
                pdfOutput = open(os.path.join(folder, os.path.splitext(filename)[0] + '_encrypted.pdf'), 'wb')
                pdfWriter.write(pdfOutput)
                pdfOutput.close()

# TODO

if len(sys.argv) < 2:
    print('Type password for encryption')
    sys.exit()
 
password = sys.argv[1]    # first command line arg is the password

encryptPdf('C:\\Users\\ahn\\Downloads\\a')