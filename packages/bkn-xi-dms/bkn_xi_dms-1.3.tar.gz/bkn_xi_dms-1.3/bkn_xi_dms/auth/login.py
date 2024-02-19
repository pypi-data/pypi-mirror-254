import getpass
import requests
import json
from bkn_xi_dms.auth.validation import *


def login(url):
    username = input('Masukkan username MySAPK : ')
    password = getpass.getpass('Masukkan password MySAPK : ')

   # url = 'https://sso-siasn.bkn.go.id/auth/realms/internal-BKN/protocol/openid-connect/token'
    url = 'https://docu-ms.bkn.go.id/uma/auth/login-asn'

    headers = {
        # 'Content-Type': 'application/x-www-form-urlencoded'
        'Content-Type': 'application/json'
    }

    payload = {
        # "client_id": client_id,
        # "grant_type": 'password',
        'password': password,
        'username': username
    }

    r = requests.request("POST", url, headers=headers,
                         json=payload, verify=False)
    result = json.loads(r.text)
    print(result)
    return result['data']['access_token']



