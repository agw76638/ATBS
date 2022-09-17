import shutil, os

def copyFile(folder):
    folder = os.path.abspath(folder)

    # Copy selected files.
    for foldername, subfolders, filenames in os.walk(folder):
        print(f'Copying files in {foldername}...')

        for filename in filenames:
            if filename.endswith('.pdf') or filename.endswith('.jpg'):
                shutil.copy(os.path.join(foldername, filename), 'C:\\Users\\ahn\\Downloads\\b')

copyFile('C:\\Users\\ahn\\Downloads\\a')