import json
import requests
import os
import shutil
from datetime import date
from os import path
from requests.packages import urllib3


def add_document(headers, employee, document, job_id, link_create_document):
    url_create_document = link_create_document
    item = {
        "documentTypeId": document["document_id"],
        "documentDate": date.today().strftime("%d/%m/%Y"),
        "retention": True,
        "isRetention": 1,
        "retentionPeriodId": 20,
        "retentionInterval": 2,
        "pagesQty": document["document_page_qty"],
        "nip": employee["nip"],
        "oldNip": "",
        "profileNik": "",
        "profileFullname": employee["name"],
        "profileInstance": "",
        "profileClass": "",
        "profileId": "",
        "jobScanId": job_id
    }
    resp = requests.post(url_create_document, headers=headers,
                         json=item, verify=False)

    if (resp.status_code == 201):
        resp = resp.json()
        document = {
            "id":  resp["data"]["id"],
            "path": document["document_path"]
        }
        return document
