import random
import string
import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from BaseAPI import TestAPI
from report_send import send_email


with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)


@pytest.fixture(scope='session')
def browser():
    if testdata['browser'] == "firefox":
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()
    send_email()

@pytest.fixture()
def token():
    t = TestAPI()
    t = t.create_token()
    return t

@pytest.fixture()
def text_tittle():
    text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    return text

@pytest.fixture()
def text_description():
    text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
    return text

@pytest.fixture()
def text_content():
    text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
    return text


@pytest.fixture()
def report_send_email():
    send_email()