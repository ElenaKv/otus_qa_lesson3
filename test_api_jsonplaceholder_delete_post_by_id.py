import requests
import pytest


@pytest.mark.parametrize('id', [1, 2, 3])
def test_delete_posts_by_id(base_url_jsonplaceholder, api_path_jsonplaceholder, id):

    api_path_jsonplaceholder = '/posts/' + str(id)

    api_request = base_url_jsonplaceholder + api_path_jsonplaceholder
    r = requests.delete(api_request)
    print(r.url)

    assert r.status_code == 200
