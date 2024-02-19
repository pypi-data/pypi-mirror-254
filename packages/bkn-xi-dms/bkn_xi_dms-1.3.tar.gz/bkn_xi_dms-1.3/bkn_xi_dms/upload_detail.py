import requests
from requests.packages import urllib3


def set_upload_document(id, path, link_upload_document, headers_upload):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    post_url = link_upload_document
    is_success = 0
    count = 0
    while count < 3 or is_success == 0:
        print("uploading file : ", path)
        files = {'RemoteFile': open(path, 'rb')}
        payload = {
            "id": id
        }
        resp = requests.post(post_url, headers=headers_upload, files=files,
                             data=payload, verify=False)
        print(resp.content)
        is_success = resp.status_code

        if is_success == 200:
            print(path, ": success to upload")
            break
        else:
            print(path, ": FAIL.... to upload")
            print("trying upload again... attemp for ", count + 1, " times")
            count += 1

        # print("====================================")
        # print("respon uploaded adalah", resp.content)
