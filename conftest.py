from pytest import fixture
import requests


def pytest_addoption(parser):
    parser.addoption('--url_dog',
                     action='store',
                     default='https://dog.ceo',
                     help='Url to make request to dog.ceo'
                     )

    parser.addoption('--api_path',
                     action='store',
                     help='api path to make request to dog.ceo'
                     )
    parser.addoption('--url_brewery',
                     action='store',
                     default='https://api.openbrewerydb.org',
                     help='Url to make request to list of breweries'
                     )
    parser.addoption('--api_path_brewery',
                     action='store',
                     help='api path to make request to list of breweries'
                     )
    parser.addoption('--url_jsonplaceholder',
                     action='store',
                     default='https://jsonplaceholder.typicode.com',
                     help='Url to make request to jsonplaceholder'
                     )
    parser.addoption('--api_path_jsonplaceholder',
                     action='store',
                     help='api path to make request to jsonplaceholder'
                     )
    parser.addoption('--url_ya',
                     action='store',
                     default='https://an.yandex.ru',
                     help='Url to make request to Yandex.ru'
                     )

    parser.addoption('--api_path_ya',
                     action='store',
                     help='api path to make request to Yandex.ru'
                     )


@fixture(scope='session')
def ya_base_url(request):
    base_url = request.config.getoption('--url_ya')
    return base_url


@fixture(scope='session')
def ya_api_path(request):
    api_path = request.config.getoption('--api_path_ya')
    return api_path


@fixture(scope="session")
def base_url(request):
    base_url = request.config.getoption('--url_dog')
    return base_url


@fixture(scope="session")
def api_path(request):
    api_path = request.config.getoption('--api_path')
    return api_path


@fixture(scope="session")
def base_url_brewery(request):
    base_url = request.config.getoption('--url_brewery')
    return base_url


@fixture(scope="session")
def api_path_brewery(request):
    api_path = request.config.getoption('--api_path_brewery')
    return api_path


@fixture(scope="session")
def base_url_jsonplaceholder(request):
    base_url = request.config.getoption('--url_jsonplaceholder')
    return base_url


@fixture(scope="session")
def api_path_jsonplaceholder(request):
    api_path = request.config.getoption('--api_path_jsonplaceholder')
    return api_path
