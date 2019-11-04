import requests
import pytest


@pytest.mark.parametrize("type", ['micro', 'regional', 'brewpub', 'large', 'planning', 'bar', 'contract', 'proprietor'])
def test_api_requests_list_of_breweries_by_type(base_url_brewery, api_path_brewery, type):

    api_path_brewery = "/breweries"
    payload = {"by_type": type}

    api_request = base_url_brewery + api_path_brewery
    r = requests.get(api_request, params=payload)
    print(r.json())

    assert r.status_code == 200
    assert r.json() != []
