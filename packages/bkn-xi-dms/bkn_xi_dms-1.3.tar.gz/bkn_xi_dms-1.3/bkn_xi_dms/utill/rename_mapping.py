
import os
from datetime import date
import PyPDF2
from os import path
from .search_employee import *
from .jenis_dokumen import *


path_directory = ""
list_employee_nip = os.listdir(path_directory)

name_mapping = {"old_filename_1.txt": "Surat Tanda Tamat Belajar.pdf",
                "old_filename_2.txt": "Transkrip Nilai.pdf",
                "old_filename_1.txt": "Daftar Riwayat Hidup.pdf",
                "old_filename_1.txt": "Pertimbangan Teknis Penetapan NIP.pdf",
                }

for folder in list_employee_nip:
    list_doc = os.listdir(path_directory + employee_nip)
    for filename in list_doc:
        if filename in name_mapping:
            old_file_path = os.path.join(list_doc, filename)
            new_filename = name_mapping[filename]
            new_file_path = os.path.join(directory, new_filename)
            os.rename(old_file_path, new_file_path)
