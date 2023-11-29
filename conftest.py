import pytest
import requests
import yaml

with open("/Users/mishinaekaterin/PycharmProjects/pythonProject4/dz1/config.yaml") as f:
    data = yaml.safe_load(f)


@pytest.fixture()
def authorization_token():
    result = requests.post(url=data['url'],
                           data={'username': data['login'],
                                 'password': data['password']})
    token = result.json()["token"]
    return token

