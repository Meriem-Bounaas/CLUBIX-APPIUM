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
        if (langue == 'Fr'):
            return bool(self.driver.find_element(By.XPATH, "//android.view.View[@text=\"Déconnexion\"]"))
        if (langue == 'Ar'):
            return bool(self.driver.find_element(By.XPATH, "//android.view.View[@text=\"تسجيل الخروج\"]"))
        if (langue == 'En'):
            return bool(self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"Logout\"]"))

    def logout(self) -> None:
        self.deconnexion_btn.click()
