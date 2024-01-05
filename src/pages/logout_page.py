from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from lib.customLib import *

from src.pages.base.base_page import BasePage


class LogoutPage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver = driver

    locators = {
        "deconnexion_btn" : ('xpath', '//*[@resource-id="deconnexionBtn"]'),
    }

    def verify_page(self, langue) -> bool:
        ''' function to verify the header of logout page'''
        return self.pages['logout'][langue]['verify_page'](self)

    def logout(self) -> None:
        ''' function to logout'''
        self.deconnexion_btn.click()