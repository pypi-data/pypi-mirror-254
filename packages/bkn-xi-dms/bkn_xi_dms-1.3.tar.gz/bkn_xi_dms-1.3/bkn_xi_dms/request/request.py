import requests
import time


def get_json_response(url, headers=None):
    retries = 3  # maximum number of retries
    for i in range(retries):
        try:
            response = requests.get(url, headers=headers, verify=False)
            response.raise_for_status()  # raise an error if the status code is not 2xx
            return response.json()  # return the JSON response data
        except ConnectionError:
            # handle connection error here
            print('Connection error')
        except requests.exceptions.HTTPError as http_err:
            # handle HTTP error here
            print(f'HTTP error occurred: {http_err}')
            return None
        except Exception as err:
            # handle other errors here
            print(f'Other error occurred: {err}')
        if i < retries - 1:
            print(f'Retrying ({i + 1}/{retries})...')
            time.sleep(2 ** i)
    return None


def get_json_response(url, headers=None, params=None):
    retries = 3  # maximum number of retries
    for i in range(retries):
        try:
            response = requests.get(
                url, headers=headers, params=params, verify=False)
            response.raise_for_status()  # raise an error if the status code is not 2xx
            return response.json()  # return the JSON response data
        except ConnectionError:
            # handle connection error here
            print('Connection error')
        except requests.exceptions.HTTPError as http_err:
            # handle HTTP error here
            print(f'HTTP error occurred: {http_err}')
            return None
        except Exception as err:
            # handle other errors here
            print(f'Other error occurred: {err}')
        if i < retries - 1:
            print(f'Retrying ({i + 1}/{retries})...')
            time.sleep(2 ** i)
    return None


def set_json_response(url, headers=None, payload=None, verify=False):
    retries = 3  # maximum number of retries
    for i in range(retries):
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # raise an error if the status code is not 2xx
            return response.json()  # return the JSON response data
        except ConnectionError:
            # handle connection error here
            print('Connection error')
        except requests.exceptions.HTTPError as http_err:
            # handle HTTP error here
            print(f'HTTP error occurred: {http_err}')
            return None
        except Exception as err:
            # handle other errors here
            print(f'Other error occurred: {err}')
        if i < retries - 1:
            print(f'Retrying ({i + 1}/{retries})...')
            time.sleep(2 ** i)
    return None
