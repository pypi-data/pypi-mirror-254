import os
from datetime import date
import PyPDF2
from os import path
from .search_employee import *
from .jenis_dokumen import *
from .report.prascan import *


def get_document_total_page(path_document):
    file = open(path_document, 'rb')

    # baca jumlah halaman
    readpdf = PyPDF2.PdfReader(file)
    totalpages = len(readpdf.pages)
    # tutup koneksi ke file
    file.close()
    return totalpages


def to_text(list, path):
    if os.path.exists(path) and os.path.getsize(path) > 0:
        with open(path, 'a') as f:
            f.write('\n'.join(list))
    else:
        with open(path, 'w') as f:
            f.write('\n'.join(list))

    print("done file at the", path)


def create_list_employee_document_by_directory(path_directory, headers, path_report_file, link_search_nip, list_document_type):

    list_employees_not_found = []
    list_documents_not_pdf = []
    list_documents_over_limit_size = []
    list_document_will_upload = []
    list_employee_nip = os.listdir(path_directory)
    list_document_job = []
    list_job = []
    list_file_not_upload = []
    for employee_nip in list_employee_nip:
        count = 0
        limit = 10
        employee = SearchEmployee()
        if employee.search_by_nip(employee_nip, headers, link_search_nip) is None:
            print("Employee Tidak Ditemukan")
            list_employees_not_found.append({"nip": employee_nip})
            continue
        list_doc = os.listdir(path_directory + employee_nip)
        base_path = os.path.join(path_directory + employee_nip)

        employee_doc = {
            "nip": employee_nip,
            "name": employee.search_by_nip(employee_nip, headers, link_search_nip).nama,
            "job_scan_id": "",
            "document": []
        }

        status = 0
        for item in list_doc:
            document_path = os.path.join(base_path, item)
            if not os.path.isfile(document_path):
                continue
            elif not document_path.endswith(".pdf"):
                list_documents_not_pdf.append(
                    {"NIP": employee_nip, "PATH": document_path})
                continue
            if os.path.getsize(document_path) > 10*1024*1000:
                list_documents_over_limit_size.append(
                    {"NIP": employee_nip, "PATH": document_path})
                continue
            document_name = item
            document_type = item.rsplit('.', 1)[0]
            document_path = os.path.join(base_path, item)
            document_page_qty = get_document_total_page(document_path)
            if count < limit:
                document = {
                    "document_id": get_jenis_file(document_name, list_document_type),
                    "document_name": document_name,
                    "document_type": document_type,
                    "document_path": document_path,
                    "document_page_qty": document_page_qty,
                    "document_date": date.today().strftime("%d/%m/%Y"),
                    "document_job_scan_id": ""
                }
                if document["document_id"] == 0:
                    list_file_not_upload.append(document_path)
                    continue
# Add Filtered Document Upload
                list_document_will_upload.append(
                    {"nip": employee_nip, "path": document_path})
                employee_doc["document"].append(document)
                count += 1
                if count == limit:
                    list_document_job.append(employee_doc)
                    status = 1
            else:
                limit += 10
                employee_doc = {
                    "nip": employee_nip,
                    "name": employee.search_by_nip(employee_nip, headers, link_search_nip).nama,
                    "job_scan_id": "",
                    "document": []
                }
                document = {
                    "document_id": get_jenis_file(document_name, list_document_type),
                    "document_name": document_name,
                    "document_type": document_type,
                    "document_path": document_path,
                    "document_page_qty": document_page_qty,
                    "document_date": date.today().strftime("%d/%m/%Y"),
                    "document_job_scan_id": ""
                }
                if document["document_id"] == 0:
                    list_file_not_upload.append(document_path)
                    continue
# Add Filtered Document Upload
                list_document_will_upload.append(
                    {"nip": employee_nip, "path": document_path})
                employee_doc["document"].append(document)
                count += 1
                status = 0
        if status == 0:
            list_document_job.append(employee_doc)

    if len(list_employees_not_found) != 0:
        create_report_excel(list_employees_not_found,
                            path_report_file, "NIP_Tidak_Ditemukan", "ffff0000")
    if len(list_documents_not_pdf) != 0:
        create_report_excel(list_documents_not_pdf,
                            path_report_file, "Bukan_PDF", "ffff0000")
    if len(list_documents_over_limit_size) != 0:
        create_report_excel(list_documents_over_limit_size,
                            path_report_file, "File_Besar", "ffff0000")
    if len(list_file_not_upload) != 0:
        create_report_excel(list_file_not_upload,
                            path_report_file, "File_miss", "ffff0000")
    if len(list_document_will_upload) != 0:
        create_report_excel(list_document_will_upload,
                            path_report_file, "Draft File Upload", "ff00ff00")
    return list_document_job
