from pprint import pprint
import requests
from reddit import Reddit
import yadisk


def test_request():
    url = "http://httpbin.org/get"
    # url = "https://cloud-api.yandex.net/v1/disk"
    params = {"model": "nike123"}
    headers = {"authorization": "secret = token - 123"}
    response = requests.get(url=url, params=params, headers=headers, timeout=5)
    pprint(response.status_code)
    if response.status_code != 200:
        print(response)

    pprint(response.json())



if __name__ == '__main__':
    test_request()
    reddit = Reddit