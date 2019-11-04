import requests


def test_api_requests(base_url, api_path):

    api_path = '/api/breed/hound/images'

    api_request = base_url + api_path
    r = requests.get(api_request)

    print(r.url)
    print(r.json())

    assert r.status_code == 200
    assert isinstance({'status': 'success'}, dict) is True
    assert r.json() != []





