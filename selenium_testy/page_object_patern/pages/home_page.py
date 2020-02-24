# -*- coding: utf-8 -*-
from base_page import BasePage
from locators import HomePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class HomePage(BasePage):

    def _verify_page(self):
        #Assertion link value
        assert u"Media Markt - Sklep internetowy mediamarkt.pl" in self.driver.title
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(HomePageLocators.LOGIN_BTN))

    def click_login_button(self):
        #Click button "Zaloguj" on main side
        element_zal = self.driver.find_element(*HomePageLocators.LOGIN_BTN)
        element_zal.click()
        print u"HomePageLocators button click success"
