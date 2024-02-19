
import os
from urllib.parse import urlencode, urljoin
import requests
import configparser
import getpass
import json
import logging
from colorlog import ColoredFormatter

# Create a custom formatter

def write_auth_token(token):
      # Create a dictionary with configuration data
    config_data = {
        'auth': {'token': token}
    }

    # Create a ConfigParser object
    config = configparser.ConfigParser()

    # Add sections and key-value pairs from the dictionary
    config.update(config_data)

    # Write the configuration to a file
    with open('auth.ini', 'w') as configfile:
        config.write(configfile)

def check_active_token(url, header):
    if requests.get(url, header, verify=False):
        return True
    else:
        print("Unauthorized access. Please check your credentials.")
        print("Token has expired")
        return False   

def check_files_in_directory(directory):
    files = os.listdir(directory)

    if files:
        print(f"There are files in the directory '{directory}'.")

    else:
        print(f"The directory '{directory}' is empty or does not exist.")
    return True

def check_nip_exist(header, id, url, params=None):

    if params is not None:
        encoded_params = urlencode(params)
        url = urljoin(url, '?' + encoded_params)

    # url = url+id
    res = requests.get(
        url=url, headers=header, verify=False).json()
    if res['status']:
        Employee = {
                    "id": "",
                    "nipBaru": res['data']['nipBaru'],
                    "nipLama": "",
                    "nama": res['data']['nama'],
                    "email": res['data']['email'],
                    "nik": "",
                    "noHp": "",
                    "tglLahir": "",
                    "instansiIndukId": "",
                    "instansiIndukNama": "",
                    "satuanKerjaIndukId": "",
                    "satuanKerjaIndukNama": "",
                    "kanregId": "",
                    "kanregNama": "",
                    "instansiKerjaId": "",
                    "instansiKerjaNama": "",
                    "instansiKerjaKodeCepat": "",
                    "golRuangAkhirId": "",
                    "golRuangAkhir": "",
                    "keycloackId": res['data']['keycloackId']
        }
        return Employee
    else:
        return None

#def screening_file (path, header, id, url, params=None ):


def read_token_from_file():
    # Check if the file exists
    if not os.path.exists('auth.ini'):
        print("The 'auth.ini' file does not exist.")
        return None

    # If the file exists, read parameters from it
    config = configparser.ConfigParser()
    config.read('auth.ini')

    # Check if the 'auth' section exists
    if 'auth' not in config:
        print("The 'auth' section is missing in the 'auth.ini' file.")
        return None

    # Check if the 'token' parameter exists in the 'auth' section
    if 'token' not in config['auth']:
        print("The 'token' parameter is missing in the 'auth' section.")
        return None

    # Return the value of the 'token' parameter
    return config.get('auth', 'token')