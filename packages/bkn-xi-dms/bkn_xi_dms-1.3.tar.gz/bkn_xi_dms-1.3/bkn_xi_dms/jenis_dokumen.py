

"""
created on Wed Feb 2023

"""
import re


def get_jenis_file(file_name, list_document_type):
    id = ""
    for keyval in list_document_type:
        name = keyval["name"]
        if re.search(name.lower(), file_name.lower()):
            id = keyval["id"]
            break
        else:
            id = 0
    return id
