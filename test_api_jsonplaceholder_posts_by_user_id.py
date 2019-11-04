import requests
import pytest


@pytest.mark.parametrize("user_id", [1, 2, 3, 4, 10])
def test_api_get_posts_by_user_id(base_url_jsonplaceholder, api_path_jsonplaceholder, user_id):

    api_path_jsonplaceholder = "/posts"
    payload = {"userId": user_id}

    api_request = base_url_jsonplaceholder + api_path_jsonplaceholder
    r = requests.get(api_request, params=payload)

    assert r.status_code == 200
    assert r.json() != []
    assert 'body' in r.text
