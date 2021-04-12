# ! python3

"""
selective_copy.py -

Write a program that walks through a folder tree and searches for files with a certain file extension (such as .pdf or
 .jpg). Copy these files from whatever location they are in to a new folder.
method
"""

import os
import shutil

# create target dir
target = r'C:\Users\Betty\Desktop\mydocs_pdf_backup'
if not os.path.exists(target):
    os.makedirs(target)

# setup a for loop
for dir, sdirs, files_names in os.walk(r'C:\Users\Betty\Documents'):
    for f in files_names:
        # id .pdfs
        if f.endswith('.pdf'):
            # copy .pdf to target
            # print(f)
            shutil.copy(os.path.join(dir, f), target)

