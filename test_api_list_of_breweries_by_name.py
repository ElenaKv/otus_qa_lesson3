import requests
import pytest


@pytest.mark.parametrize("name", ["Trim Tab Brewing", "Yellowhammer Brewery", "Bearpaw River Brewing Co"])
def test_api_requests_list_of_breweries_by_name(base_url_brewery, api_path_brewery, name):

    api_path_brewery = "/breweries"
    payload = {"by_name": name}

    api_request = base_url_brewery + api_path_brewery
    r = requests.get(api_request, params=payload)
    print(r.json())

    assert r.status_code == 200
    assert r.json() != []
