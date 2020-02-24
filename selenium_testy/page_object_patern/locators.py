# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

class HomePageLocators():
    """ Locators home page """
    LOGIN_BTN = (By.XPATH, '//*[@class="js-header_login"]')

class LoginPageLocators():
    """ Locators login account page """
    LOG_BTN = (By.XPATH, '//button[@class="gua-login m-btn m-btn_primary"]')
    CLOSE_X_BUTTON = (By.XPATH, '//*[@id="js-cookieInfo_confirm"]')
    ERROR_LOGIN_VALIDATION_NOTICES_MESSAGE = (By.XPATH, '//*[@for="enp_customer_form_login_username"][@style="display: block;"]')
    ERROR_PAASSWORD_VALIDATION_NOTICES_MESSAGE = (By.XPATH, '//*[@for="enp_customer_form_login_password"][@style="display: block;"]')
    CREATE_ACCOUNT_BTN = (By.XPATH, '//*[@class="m-btn m-btn_primary is-submitBtn"]')

class RegistrationPageLocators():
    """ Locators registraction page """
    REGISTRACTION_BUTTON = (By.XPATH, '//*[@class="m-btn m-btn_primary js-register_submit"]')
    ERROR_VALIDATION_RADIO = (By.XPATH, '//*[@for="enp_customer_registration_form_type[address][salutation]"]')
    ERROR_VALIDATION_NAME_FIELD = (By.XPATH, '//*[@for="enp_customer_registration_form_type_address_firstName"][@class="invalid"]')
    ERROR_VALIDATION_SURNAME_FIELD = (By.XPATH, '//*[@for="enp_customer_registration_form_type_address_lastName"][@class="invalid"]')
    ERROR_VALIDATION_E_MAIL_FIELD = (By.XPATH, '//*[@for="enp_customer_registration_form_type_email"][@class="invalid"]')
    ERROR_VALIDATION_PASSWORD_FIELD = (By.XPATH, '//*[@for="enp_customer_registration_form_type_plainPassword"][@class="invalid"]')
    ERROR_VALIDATION_PHONE_NUMBER = (By.XPATH, '//*[@for="enp_customer_registration_form_type_mobileNumber_number"][@class="invalid"]')
    ERROR_VALIDATION_POSTAL_CODE = (By.XPATH, '//*[@for="enp_customer_registration_form_type_address_postcode"][@class="invalid"]')
    ERRPR_ALL_VALIDATION_FIELD = (By.XPATH, '//*[@class="m-form_field state-error"]/em')
