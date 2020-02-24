# -*- coding: utf-8 -*-
from base_page import BasePage
from locators import LoginPageLocators

class LoginPage(BasePage):

    def _verify_page(self):
        assert u"MediaMarkt" in self.driver.title

    def click_log_button(self):
        """Click button to login account"""
        element = self.driver.find_element(*LoginPageLocators.LOG_BTN)
        element.click()
        print u"Login click button Zaloguj success"

    def exit_x_button(self):
        """Tourn off cookie message"""
        element = self.driver.find_element(*LoginPageLocators.CLOSE_X_BUTTON)
        element.click()
        print u"Cookie message tourn off success"

    def error_login_validation_message(self):
        """Validation error message field e_mail"""
        error_message = self.driver.find_element(*LoginPageLocators.ERROR_LOGIN_VALIDATION_NOTICES_MESSAGE)
        assert error_message.is_displayed(), u"Nieprawidłowy adres email"
        print u"Login validation message email success"

    def error_passwor_validation_message(self):
        """Validation error message field password"""
        error_message = self.driver.find_element(*LoginPageLocators.ERROR_PAASSWORD_VALIDATION_NOTICES_MESSAGE)
        assert error_message.is_displayed(), u"Podaj hasło"
        print u"Login validation message password success"

    def click_craete_new_account(self):
        """Click button Zaluz konto"""
        element = self.driver.find_element(*LoginPageLocators.CREATE_ACCOUNT_BTN)
        element.click()
        print u"Login click button Zaluz konto success"

    def check_if_no_error_notice_is_presented(self):
        """Check if there are no validatio error message"""
        error_notices = self.driver.find_elements(*LoginPageLocators.ERROR_PAASSWORD_VALIDATION_NOTICES_MESSAGE)
        for error in error_notices:
            assert not error.is_displayed(), error.get_attribute("innerText")
            print u"Login validation message check success"
