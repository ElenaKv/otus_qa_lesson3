import requests
import pytest


@pytest.mark.parametrize("user_input", ['dog', '80439', 'Arizona'])
def test_api_requests_list_of_brewery_search(base_url_brewery, api_path_brewery, user_input):
    api_path_brewery = "/breweries/search"
    payload = {"query": user_input}

    api_request = base_url_brewery + api_path_brewery
    r = requests.get(api_request, params=payload)

    assert r.status_code == 200
    assert user_input in r.text
