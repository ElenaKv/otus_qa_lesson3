import requests


def test_api_requests(base_url, api_path):

    api_path = '/api/breeds/image/random'

    api_request = base_url + api_path
    r = requests.get(api_request)
    for key, value in dict(r.json()).items():
        print(key, ' => ', value)
    assert isinstance({'status': 'success'}, dict) is True
    assert r.json() != []
    assert r.status_code == 200
