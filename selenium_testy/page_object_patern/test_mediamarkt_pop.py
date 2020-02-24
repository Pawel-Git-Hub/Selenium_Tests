# -*- coding: utf-8 -*-
import unittest
import time
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.registraction_page import RegistrationPage
from selenium import webdriver


class MediaMarktLogin(unittest.TestCase):
    def setUp(self):
        # Run Firefox
        profile = webdriver.FirefoxProfile()
        profile.set_preference("dom.webnotifications.enabled", False)
        self.driver = webdriver.Firefox(firefox_profile = profile)
        # Maximizing browser window
        self.driver.maximize_window()
        # Web page utl
        self.driver.get("https://mediamarkt.pl/")

    def tearDown(self):
        # Turn off browser
        self.driver.quit()

    def test_correct_login_account(self):
        home_page = HomePage(self.driver)
        # Click button login
        home_page.click_login_button()
        login_page = LoginPage(self.driver)
        # Timeout 4 sec
        time.sleep(4)
        # Close cookie message
        login_page.exit_x_button()
        # Timeout 4 sec
        time.sleep(4)
        # Check if there are presented error validation message
        login_page.check_if_no_error_notice_is_presented()
        # Click login button
        login_page.click_log_button()
        # Validation error message in field e-mail
        login_page.error_login_validation_message()
        # Validation error message in field password
        login_page.error_passwor_validation_message()


class MeidaMarktRegistrationUnCorrect(unittest.TestCase):
    def setUp(self):
        # Run Firefox
        profile = webdriver.FirefoxProfile()
        profile.set_preference("dom.webnotifications.enabled", False)
        self.driver = webdriver.Firefox(firefox_profile = profile)
        # Maximizing browser window
        self.driver.maximize_window()
        # Web page utl
        self.driver.get("https://mediamarkt.pl/")

    def tearDown(self):
        # Turn off browser
        self.driver.quit()

    def test_uncorrect_validation_create_account(self):
        home_page = HomePage(self.driver)
        # Click button "Zalogu sie"
        home_page.click_login_button()
        # Timeout 4 sec
        time.sleep(4)
        login_page = LoginPage(self.driver)
        # Timeout 4 sec
        time.sleep(4)
        # Timeout 4 sec
        login_page.exit_x_button()
        # Timeout 4 sec
        time.sleep(4)
        # Click on button "Zaloz konto"
        login_page.click_craete_new_account()
        # Timeout 4 sec
        time.sleep(4)
        registraction_page = RegistrationPage(self.driver)
        # Timeout 10 sec
        time.sleep(10)
        # Check if there are presented error validation message
        registraction_page.error_validation_notice_is_no_presented()
        # Click on button "Zarejestruj sie"
        registraction_page.registration_button()
        # Validation error message field chose salutation
        registraction_page.error_choose_gender()
        # Validation error message field name
        registraction_page.error_name_field()
        # Validation error message field surname
        registraction_page.error_surname_field()
        # Validation error message field e_mail
        registraction_page.error_e_mail_field()
        # Validation error message field password
        registraction_page.error_password_field()
        # Validation error message field phone number
        registraction_page.error_phone_field()
        # Validation error message field zip code
        registraction_page.error_pstal_code_field()


if __name__ == '__main__':
    unittest.main(verbosity=2)
