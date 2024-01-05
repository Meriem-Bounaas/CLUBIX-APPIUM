from appium.webdriver.webdriver import WebDriver
from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.common.by import By
from lib.customLib import *


class BasePage(PageFactory):
    def __init__(self, driver: WebDriver) -> None:
        super().__init__()
        self.driver = driver
    locators ={
    }

    def select_sport(self, langue) -> None:
        if (langue == 'Fr'):
            return self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"Quel Sport ?\"]").click()
        if (langue == 'Ar'):
            return self.driver.find_element(By.XPATH, "//android.widget.TextView[@text='أي نوع من الرياضة؟']").click()
        if (langue == 'En'):
            return self.driver.find_element(By.XPATH, "//android.widget.TextView[@text='Which Sport?']").click()
          
    def verify_header_add_group(self, langue) -> bool:
        if (langue == 'Fr'):
            return bool(self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"Ajouter un Groupe\"]"))
        if (langue == 'Ar'):
            return bool(self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"إضافة مجموعة\"]"))
        if (langue == 'En'):
            return bool(self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"Add a Group\"]"))