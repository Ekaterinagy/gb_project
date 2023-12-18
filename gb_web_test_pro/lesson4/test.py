import requests
from BaseAPI import TestAPI
from testpage import OperationsHelper
import logging
import yaml
from gb_web_test_pro.lesson4 import util

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)


def test_api_create_post(token, text_tittle, text_description, text_content):
    # Проверка создания поста
    logging.info('Test_api_create_post starting')
    test_api = TestAPI()
    test_api.create_create_post(token, text_tittle, text_description, text_content)
    result = test_api.get_post_my(token)
    description_list = test_api.check_description(result)
    logging.info(f'Test completed with result: {text_description} in {description_list}')
    assert text_description in description_list


def test_api_find_post(token, text_tittle, text_description,text_content):
    # Проверка наличия определенного заголовка и отсутвия созданого пользователем поста в не его постах
    logging.info('Test_api_find_post starting')
    test_api = TestAPI()
    test_api.create_create_post(token, text_tittle, text_description, text_content)

    res = util.avt(token)
    tittle_list = [i['title'] for i in res]
    logging.info( f'Test completed with result: {tittle_list}, {text_tittle} not in {tittle_list}')
    assert 'Котик' in tittle_list and text_tittle not in tittle_list


def test_ui_auth_wrong(browser):
    # Проверка невозможности авторизации без валидного пароля и логина
    logging.info('Test_ui_auth_wrong starting')
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login('test')
    testpage.enter_pass('test')
    testpage.click_login_button()
    assert testpage.get_error_text() == '401'


def test_ui_auth_successfully(browser):
    # Проверка авторизации с валидными логином и паролем
    logging.info('Test_ui_auth_successfully starting')
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata['name'])
    testpage.enter_pass(testdata['passwd'])
    testpage.click_login_button()
    assert testpage.get_result_auth() == "Blog"


def test_ui_create_post(browser, text_tittle, text_description, text_content):
    # Проверка создания поста с валидными данными
    logging.info('Test_ui_create_post starting')
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.click_create_post_button()
    testpage.create_tittle_post(text_tittle)
    testpage.create_description_post(text_description)
    testpage.create_content_post(text_content)
    testpage.click_button_save_post()
    assert testpage.get_result_public_post() == text_tittle


def test_ui_contact_us(browser):
    # Проверка работы формы обратной связи
    logging.info('Test_ui_contact_us starting')
    testpage = OperationsHelper(browser)
    testpage.click_contact()
    testpage.enter_name_to_contact_us('Test')
    testpage.enter_email_to_contact_us('sdff@mail.ru')
    testpage.enter_content_to_contact_us('Verification')
    testpage.click_contact_us_btn()
    assert testpage.checkout_alert() == 'Form successfully submitted'


def test_iu_log_out(browser):
    # Выход из профиля пользователя
    logging.info('Test_iu_log_out starting')
    testpage = OperationsHelper(browser)
    testpage.log_out()
    assert testpage.get_result_login_out() == 'LOGIN'
    logging.info('Logout completed')