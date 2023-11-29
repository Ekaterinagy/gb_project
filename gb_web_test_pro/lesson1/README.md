## Урок 1. Реализация тестирования API с использованием DDT

### Задание

Добавить фикстуру для авторизации, проверить существует ли пост по идентификатору


```
@pytest.fixture()
def authorization_token():
    result = requests.post(url=data['url'],
                           data={'username': data['login'],
                                 'password': data['password']})
    token = result.json()["token"]
    return token
```


```commandline
============================= test session starts =============================
collecting ... collected 1 item

test1.py::test_pagination_check_id PASSED                                [100%]

============================== 1 passed in 6.89s ==============================

Process finished with exit code 0
```

### Задание 1

Условие: Добавить в задание с REST API ещё один тест, в котором создаётся новый пост, а потом проверяется его наличие на
сервере по полю «описание».

Подсказка: создание поста выполняется запросом к https://test-stand.gb.ru/api/posts с передачей параметров title,
description, content.

Что ещё можно почитать:
• Описание Wikipedia API
• Пример использования zeep

```
def test_post_method(authorization_token):
    rnd_uuid, post_id = create_post(authorization_token)
    post_json = get_post(authorization_token, post_id)
    assert 1 == 1 and post_json is not None and post_json['id'] == post_id and rnd_uuid in post_json[
        'content'], 'Test Failed'
```


```commandline
============================= test session starts =============================
collecting ... collected 1 item

test1.py::test_post_method PASSED                                        
[100%]response_json {'id': 90535, 'title': 'Ek186aecc7d-e5a9-4100-ae9c-d8de73f1d457', 'description': 'Ek1Desc86aecc7d-e5a9-4100-ae9c-d8de73f1d457', 'content': 'Ek1Content86aecc7d-e5a9-4100-ae9c-d8de73f1d457', 'authorId': 22986, 'mainImage': {'id': None, 'cdnUrl': ''}, 'updatedAt': '2023-11-29T11:04:40+00:00', 'createdAt': '2023-11-29T11:04:40+00:00', 'labels': [], 'delayPublishTo': None, 'draft': False}

============================== 1 passed in 2.07s ==============================
```

