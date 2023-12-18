import logging
import requests
import yaml

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)


class TestAPI:
    def __init__(self):
        self.base_url = 'https://test-stand.gb.ru/'

    def create_token(self):
        try:
            result = requests.post(url=self.base_url + testdata['login_site'],
                                   data={"username": testdata['name'], "password": testdata['passwd']})
            token = result.json()["token"]
            return token
        except:
            logging.exception('Exception with token')
        return None

    def create_create_post(self, token, text_tittle, text_description, text_content ):
        try:
            requests.post(url=self.base_url+testdata['post_site'], headers={"X-Auth-Token": token},
                      params={"title": text_tittle, "description": text_description, "content": text_content})
            return True
        except:
            logging.exception('Exception with create post')
            return False

    def get_post_my(self, token):
        try:
            res_get = requests.get(url=self.base_url+testdata['post_site'],
                                   headers={"X-Auth-Token": token}, params={"owner": 'Me'})
            return res_get
        except:
            logging.exception('Exception with request')
            return None

    def check_description(self, result):
        try:
            description_list = [i['description'] for i in result.json()['data']]
            return description_list
        except:
            logging.exception('Exception with description_list')
            return None

    def get_post_list_not_me(self, token):
        try:
            res_get = requests.get(url=self.base_url+testdata['post_site'],
                                   headers={"X-Auth-Token": token}, params={"owner": "notMe"})
            return res_get
        except:
            logging.exception('Exception with get tittle list')
            return None

    def check_tittle_list(self, result):
        try:
            tittle_list = [i['title'] for i in result.json()['data']]
            return tittle_list
        except:
            logging.exception('Exception with tittle_list')
            return None