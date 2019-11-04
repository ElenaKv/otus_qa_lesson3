import requests


def test_api_requests(base_url, api_path):

    api_path = '/api/breed/hound/list'

    api_request = base_url + api_path
    r = requests.get(api_request)

    print(r.json())
    print(r.headers)
    print(r.request)
    print(r.reason)

    assert r.status_code == 200
    assert r.json() != []





    
