import requests


def test_get_posts(base_url_jsonplaceholder, api_path_jsonplaceholder):

    api_path_jsonplaceholder = "/posts/1/comments"

    api_request = base_url_jsonplaceholder + api_path_jsonplaceholder
    r = requests.get(api_request)
    print(r.url)
    print(r.json())

    assert r.status_code == 200
















