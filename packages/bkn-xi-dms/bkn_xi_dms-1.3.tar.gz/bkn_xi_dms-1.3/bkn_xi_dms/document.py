from datetime import date
import os
import shutil
from bkn_xi_dms.report.r_logger import * 

def set_document (job:None,doc:None):
        obj = {
        "documentTypeId": doc['doc_type'],
        "documentDate": date.today().strftime("%d/%m/%Y"),
        "retention": True,
        "isRetention": 1,
        "retentionPeriodId": 20,
        "retentionInterval": 2,
        "pagesQty": 1,
        "nip": doc['employee']["nipBaru"],
        "oldNip": "",
        "profileNik": "",
        "profileFullname": doc['employee']["nama"],
        "profileInstance": "",
        "profileClass": "",
        "profileId": "",
        "jobScanId": job["data"]["id"]
    }
        return obj

def move_file(src_path, dest_path, l):
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    shutil.move(src_path, dest_path)
    l.info(f"moving file {src_path}")