import json
import requests


def createJobScan(headers, link_create_job):
    url_create_job = link_create_job

    jsonc = {
        "createdById": "null",
        "createdDate": "null",
        "documentQty": 0,
        "id": "null",
        "remarks": "",
        "runnerName": "null",
        "runnerNip": "null",
        "status": "null",
        "uniqueCode": "null",
        "updateDate": "null"
    }
    resp = requests.post(url_create_job, headers=headers,
                         json=jsonc, verify=False)
    if (resp.status_code == 201):
        return resp.json()
    else:
        print("!!!!!!!!!!!!!!!!error create Job!!!!!!!!!!!!!!!!!!!!")
        print("!!!!!!!!!!!!!!!!error create Job!!!!!!!!!!!!!!!!!!!!")
        print(resp.json())
        return resp.json()
