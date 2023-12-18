from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import yaml


class TestSearchLocators:
    ids = dict()
    with open('locators.yaml') as f:
        locators = yaml.safe_load(f)
    for locator in locators['xpath'].keys():
        ids[locator] = (By.XPATH, locators['xpath'][locator])
    for locator in locators['css'].keys():
        ids[locator] = (By.CSS_SELECTOR, locators['css'][locator])


class OperationsHelper(BasePage):

    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f'Send {word} to element {element_name}')
        field = self.find_element(locator)
        if not field:
            logging.error(f'Element {locator} not found')
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f'Exception while operation with {locator}')
            return False
        return True

    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception('Exception with click')
            return False
        logging.debug(f'Clicked {element_name} button')
        return True

    def get_text_from_element(self, locator, description):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=3)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f'Exception while get text from {element_name}')
            return None
        logging.debug(f'We find text {text} in field {element_name}')
        return text

    # ENTER
    def enter_login(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_LOGIN_FIELD'], word, description='login form')

    def enter_pass(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_PASS_FIELD'], word, description='password form')

    def create_tittle_post(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_TITTLE_FIELD'], word, description='tittle post form')

    def create_description_post(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_DESCRIPTION_FIELD'], word, description='description post form')

    def create_content_post(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_CONTENT_FIELD'], word, description='content post form')

    def enter_name_to_contact_us(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_CONTACT_NAME_FIELD'], word, description='name contact form')

    def enter_email_to_contact_us(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_CONTACT_EMAIL_FIELD'], word, description='email contact form')

    def enter_content_to_contact_us(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_CONTACT_CONTENT_FIELD'], word, description='content contact form')

    # CLICK
    def click_login_button(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_LOGIN_BTN'], description='login')

    def click_create_post_button(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_CREATE_POST_BTN'], description='create post')

    def click_button_save_post(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_SAVE_POST_BTN'], description='save post')

    def click_contact(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_CONTACT_FIELD'], description='contact')

    def click_contact_us_btn(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_CONTACT_US_BTN'], description='contact us')

    def log_out(self):
        self. click_button(TestSearchLocators.ids['LOCATOR_PROFILE_FIELD'], description='profile')
        self.click_button(TestSearchLocators.ids['LOCATOR_LOGOUT_FIELD'], description='logout')

    # GET
    def get_error_text(self):
        return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_ERROR_FIELD'], description='login')

    def get_result_auth(self):
        return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_LOGIN_RESULT'], description='after login')

    def get_result_public_post(self):
        return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_SAVE_POST_RESULT'], description='post tittles')

    def checkout_alert(self):
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        text = self.get_alert_text()
        alert = self.driver.switch_to.alert
        alert.accept()
        logging.info(f'We find {text} in alert when click to {TestSearchLocators.ids["LOCATOR_CONTACT_US_BTN"]}')
        return text

    def get_result_login_out(self):
        return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_LOGIN_BTN'], description='after logout')