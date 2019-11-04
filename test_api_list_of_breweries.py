import requests


def test_api_request_breweries(base_url_brewery, api_path_brewery):

    api_path_brewery = "/breweries"
    api_request = base_url_brewery + api_path_brewery
    r = requests.get(api_request)

    assert r.status_code == 200
    assert r.json() != []
