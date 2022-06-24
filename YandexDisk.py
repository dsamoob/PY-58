import requests
import json

class YandexDisk:
    def __init__(self, token):
        self.token = token


    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def get_files_list(self):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files?limit=1000'
        headers = self.get_headers()
        response = requests.get(files_url, headers=headers)
        return response.json()

    def _get_upload_link(self, disk_file_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        response_href = self._get_upload_link(disk_file_path=disk_file_path)
        print(response_href)
        url = response_href.get("href", "")
        response = requests.put(url, data=open(filename, 'rb'))
        print(response)
        response.raise_for_status()
        if response.status_code == 201:
            print('success')

    def make_new_directory(self, dirname: str):
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = self.get_headers()
        response = requests.put(f'{url}?path={dirname}', headers=headers)
        response.raise_for_status()
        if response.status_code == 201:
            print('success')

    def delete_file(self, file):
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = self.get_headers()
        response = requests.delete(f'{url}?path={file}', headers=headers)
        response.raise_for_status()
        if response.status_code == 204:
            print('success')






