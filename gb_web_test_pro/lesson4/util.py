# Написать тест с использованием pytest и requests, в котором:
import uuid

import requests
import yaml

# Адрес сайта, имя пользователя и пароль хранятся в config.yaml
# conftest.py содержит фикстуру авторизации по адресу
# https://test-stand.gb.ru/gateway/login с передачей параметров “username" и
# "password" и возвращающей токен авторизации
# Тест с использованием DDT проверяет наличие поста
# с определенным заголовком в списке постов другого пользователя, для этого
# выполняется get запрос по адресу https://test-stand.gb.ru/api/posts c
# хедером, содержащим токен авторизации в параметре "X-Auth-Token".
# Для отображения постов другого пользователя передается "owner": "notMe".
# http://restapi.adequateshop.com/api/authaccount/registration
# http://restapi.adequateshop.com/api/authaccount/login
# kitty89
# 61d96a3985


def avt(authorization_token):
    page = 1
    all_data = []
    # так как общее количество постов превышает 50тыс добален лимит на 10 страниц
    while page and 0 < page < 10:
        response_json = get_data(authorization_token, page)
        all_data.extend(response_json['data'])
        page = response_json["meta"]['nextPage']
    return all_data


def get_data(authorization_token: str, page: int):
    res_get = requests.get(url="https://test-stand.gb.ru/api/posts",
                           headers={"X-Auth-Token": authorization_token},
                           params={"owner": "notMe", "page": page})
    return res_get.json()


def create_post(authorization_token):
    url = 'https://test-stand.gb.ru/api/posts'
    rnd_uuid = str(uuid.uuid4());
    test_data = {'title': 'Ek1' + rnd_uuid, 'description': 'Ek1Desc' + rnd_uuid, 'content': 'Ek1Content' + rnd_uuid}
    response_json = requests.post(url=url, json=test_data, headers={"X-Auth-Token": authorization_token}).json()
    return rnd_uuid, response_json['id']


def get_post(authorization_token, post_id):
    url = f'https://test-stand.gb.ru/api/posts/{post_id}'
    response_json = requests.get(url=url, headers={"X-Auth-Token": authorization_token}).json()
    return response_json
