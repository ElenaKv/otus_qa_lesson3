import requests
import pytest


@pytest.mark.parametrize("id", [1, 2, 3, 4])
def test_api_get_post_with_id(base_url_jsonplaceholder, api_path_jsonplaceholder, id):
    api_path_jsonplaceholder = "/posts/"
    data = id

    api_request = base_url_jsonplaceholder + api_path_jsonplaceholder
    r = requests.get(api_request + str(data))
    print(r.url)

    assert r.status_code == 200
    assert id in r.json().values()
