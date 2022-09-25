import PyPDF2, os, sys

# Go through folder.
for foldername, subfolders, filenames in os.walk(folder):
    for filename in filenames:
        # TODO Encrypt PDF using a password provided on the command line.
        if filename.endswith('.pdf'):
            pdfFile = open(filename, 'rb')
            pdfWriter = PyPDF2.PdfFileWriter(pdfFile)
            pdfWriter.encrypt()

# TODO Save encrypted PDF with an _encrypted.pdf suffix