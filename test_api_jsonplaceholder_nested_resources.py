import requests
import pytest


@pytest.mark.parametrize('nested_resources', ['/posts/1/comments',
                                              '/albums/1/photos',
                                              '/users/1/albums',
                                              '/users/1/todos',
                                              '/users/1/posts'])
def test_nested_resources(base_url_jsonplaceholder, api_path_jsonplaceholder, nested_resources):

    api_path_jsonplaceholder = nested_resources

    api_request = base_url_jsonplaceholder + api_path_jsonplaceholder
    r = requests.get(api_request)
    print(r.url)

    assert r.status_code == 200
