from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from lib.customLib import *

from src.pages.base.base_page import BasePage


class GroupsPage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver = driver

    locators = {
        "toaster_succesfully_saved" : ('xpath', '//android.view.ViewGroup[@content-desc="succesfully saved"]'),
    }

    def verify_page(self, langue) -> bool:
        ''' function to verify the header of group's page'''
        if (langue == 'Fr'):
            return bool(self.driver.find_element(By.XPATH, "//android.view.View[@text=\"Mes Groupes\"]"))
        if (langue == 'Ar'):
            return bool(self.driver.find_element(By.XPATH, "//android.view.View[@text=\"مجموعاتي\"]"))
        if (langue == 'En'):
            return bool(self.driver.find_element(By.XPATH, "//android.view.View[@text=\"My Groups\"]"))
    
    def verify_add_succesfully(self) -> bool:
        ''' function to verify the succuss of save'''
        sport = read_from_csv_file('sports.csv')
        return bool(self.toaster_succesfully_saved) and self.driver.find_element(By.XPATH, "//android.widget.TextView[@resource-id=\"sportNameText\"]").text == sport[0]