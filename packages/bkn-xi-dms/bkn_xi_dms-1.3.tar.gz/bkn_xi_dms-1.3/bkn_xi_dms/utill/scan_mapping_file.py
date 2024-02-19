# scan all file if there any not in mapping name will be write in text document
import os
import pickle


def to_text(list, path):
    with open(path, 'w') as f:
        f.write('\n'.join(list))
        # pickle.dump(list, f)

    print("done file at the", path)


path = "C:\\Users\\Rifo\\Desktop\\output.txt"
path_from = "c:\\dmsUploadExperiment2\\"

list_employee_nip = os.listdir(path_from)
list_files = []

name_mapping = {"Surat Tanda Tamat Belajar.pdf": "Surat Tanda Tamat Belajar.pdf",
                "old_filename_2.txt": "Transkrip Nilai.pdf",
                "old_filename_1.txt": "Daftar Riwayat Hidup.pdf",
                "old_filename_1.txt": "Pertimbangan Teknis Penetapan NIP.pdf",
                }

for folder in list_employee_nip:
    list_doc = os.listdir(path_from + folder)
    for filename in list_doc:
        if filename not in name_mapping:
            # item_file = {
            #     "nama": filename,
            #     "path":  os.path.join(path_from + folder)
            # }
            # list_files.append(item_file)
            list_files.append(os.path.join(
                path_from + folder + "\\" + filename))
to_text(list_files, path)
