import requests


def test_api_request_to_yandex(ya_base_url, ya_api_path):
    ya_api_path = '/jserr/1'

    api_request = ya_base_url + ya_api_path
    r = requests.get(api_request)

    print(r.url)

    assert r.status_code == 200
