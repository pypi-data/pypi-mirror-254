from requests.packages import urllib3
import requests


class SearchEmployee:

    class Employee:
        nip_baru = ""
        nama = ""
        key_cloack_id = ""

    def search_by_nip(self, id, headers, link_search_nip):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        url_get_pegawai = link_search_nip+id
        res_search = requests.get(
            url=url_get_pegawai, headers=headers, verify=False)
        if (res_search.status_code) == 200:
            employee = self.Employee()
            rs_json = res_search.json()
            employee.nip_baru = rs_json['data']['nipBaru']
            employee.nama = rs_json['data']['nama']
            employee.key_cloack_id = rs_json['data']['keycloackId']
            return employee
        else:
            return None
