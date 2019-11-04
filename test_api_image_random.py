import random
import requests
from pytest import fixture
from pytest import mark


@fixture(scope="function")
def define_breed_list(base_url, api_path):
    """
    Из запроса https://dog.ceo/api/breeds/list/all
    получаем список пород в виде ключ:значение  {'affenpinscher': [],
             'african': [],
             'airedale': [],
             'akita': []...}

    """
    api_path = '/api/breeds/list/all'
    r = requests.get(base_url + api_path)

    for key, value in r.json().items():
        if key == "message":
            not_list_of_breed_yet = value
            breeds = list(dict(not_list_of_breed_yet).keys())
            return breeds
        else:
            raise Exception("Не удалось получить словарь пород.")


@fixture()
@mark.parametrize(scope="session", params=[define_breed_list])
def path_api_image_random(define_breed_list):
    """
    Получаем рандомное значение из списка пород,
    """
    random_breed = random.choice(define_breed_list)

    """
    Добавляем полученное значения в path API запроса, возвращаем path

    """
    first_part_of_api_path = "/api/breed/"
    end_part_of_api_path = "/images/random"

    api_path = first_part_of_api_path + random_breed + end_part_of_api_path
    return api_path


def test_api_image_random(base_url, path_api_image_random):
    """
    Тестовая функция
    base_url: основной url API запросов
    path_api_image_random: path API запроса для получение рандомных фотографий

    """

    url = base_url + path_api_image_random
    r = requests.get(url)
    print(url)

    assert r.status_code == 200
