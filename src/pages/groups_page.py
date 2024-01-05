from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from lib.customLib import *

from src.pages.base.base_page import BasePage


class GroupsPage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver = driver

    locators = {
        "name_group_input" : ('xpath', '//*[@resource-id="nameTextInput"]'),
        "free_input" : ('xpath', '//*[@resource-id="feesTextInput"]'),
        "save_btn" : ('xpath', '//*[@resource-id="submitBtn"]'),
        "toaster_succesfully_saved" : ('xpath', '//android.view.ViewGroup[@content-desc="succesfully saved"]')
    }

    def verify_page(self, langue) -> bool:
        ''' function to verify the header of group's page'''
        return self.pages['groups'][langue]['verify_page'](self)
        
    def add_group(self, langue) -> str:
        groups_list = ['femme_A1' , 'femme_A2', 'Homme_A1', 'Homme_A2', 'Enfant_A1', 'Enfant_A2']
        group = random.choice(groups_list)
        free = random.randint(50, 200)
        self.add_btn.click()
        self.verify_header_add_group(langue)
        self.name_group_input.set_text(group)
        self.select_sport(langue)
    
        sport = read_from_csv_file('sports.csv')
        sport_element = self.driver.find_element(By.XPATH, f"//android.view.ViewGroup[@content-desc=\"{sport[0]}\"]")
        sport_element.click()

        self.free_input.set_text(free)
        self.save_btn.click()

        save_in_csv_file('groups.csv', ['group'], [group])
    
    def verify_add_succesfully(self) -> bool:
        ''' function to verify the succuss of save'''
        sport = read_from_csv_file('sports.csv')
        return bool(self.toaster_succesfully_saved) and self.driver.find_element(By.XPATH, "//android.widget.TextView[@resource-id=\"sportNameText\"]").text == sport[0]