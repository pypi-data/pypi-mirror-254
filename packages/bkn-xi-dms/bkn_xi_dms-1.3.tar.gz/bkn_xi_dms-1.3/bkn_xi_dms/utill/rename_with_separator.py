# turn document name from : nama dokument_nip to nama_dokument

import os
from datetime import date
import PyPDF2
from os import path


path_directory = "c:\\dmsUploadExperiment2\\"
list_employee_nip = os.listdir(path_directory)

separator = "_"

for folder in list_employee_nip:
    list_doc = os.listdir(path_directory + folder)
    base_path = os.path.join(path_directory + folder)
    for filename in list_doc:
        old_file_path = os.path.join(base_path, filename)
        new_filename = filename.split(
            separator)[0] + os.path.splitext(filename)[1]
        new_file_path = os.path.join(base_path, new_filename)
        print(new_file_path)
        os.rename(old_file_path, new_file_path)
