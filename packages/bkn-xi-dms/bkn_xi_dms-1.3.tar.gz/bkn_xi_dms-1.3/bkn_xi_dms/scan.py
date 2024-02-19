
import requests
from bkn_xi_dms.report.r_logger import * 

def setJobScanData():
    obj = {
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
    return obj

def sendJobScan(url, header, l):
    obj = setJobScanData()
    res = requests.post(url, headers=header, json=obj, verify=False)
    if res.status_code == 201:
        return res.json()
    else:
        l.error(f"Fail Generate Job / sending request post {res.status_code}")
        return res.json()