from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from lib.customLib import *

from src.pages.base.base_page import BasePage


class GroupsPage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver = driver

    locators = {
        "add_btn" : ('xpath', '//*[@resource-id="addBtn"]'),
        "name_group_input" : ('xpath', '//*[@resource-id="nameTextInput"]'),
        "free_input" : ('xpath', '//*[@resource-id="feesTextInput"]'),
        "save_btn" : ('xpath', '//*[@resource-id="submitBtn"]'),
        "toaster_succesfully_saved" : ('xpath', '//*[@resource-id="succesfully saved"]'),
    }

    def verify_page(self, langue) -> bool:
        if (langue == 'Fr'):
            return bool(self.driver.find_element(By.XPATH, "//android.view.View[@text=\"Mes Groupes\"]"))
        if (langue == 'Ar'):
            return bool(self.driver.find_element(By.XPATH, "//android.view.View[@text=\"مجموعاتي\"]"))
        if (langue == 'En'):
            return bool(self.driver.find_element(By.XPATH, "//android.view.View[@text=\"My Groups\"]"))
    
    def verify_header_add_group(self, langue) -> bool:
        if (langue == 'Fr'):
            return bool(self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"Ajouter un Groupe\"]"))
        if (langue == 'Ar'):
            return bool(self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"إضافة مجموعة\"]"))
        if (langue == 'En'):
            return bool(self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"Add a Group\"]"))
    
    def select_sport(self, langue):
        if (langue == 'Fr'):
            return self.driver.find_element(By.XPATH, "//*[@resource-id='Quel Sport ?']")
        if (langue == 'Ar'):
            return self.driver.find_element(By.XPATH, "//*[@resource-id='أي نوع من الرياضة؟']")
        if (langue == 'En'):
            return self.driver.find_element(By.XPATH, "//*[@resource-id='Which Sport?']")

    def add_group(self, langue) -> str:
        groups_list = ['femme_A1' , 'femme_A2', 'Homme_A1', 'Homme_A2', 'Enfant_A1', 'Enfant_A2']
        group = random.choice(groups_list)
        free = random.randint(50, 200)
        self.add_btn.click()
        self.verify_header_add_group(langue)
        self.name_group_input.set_text(group)

        select_sport_element = self.select_sport(langue)
        select_sport_element.click()
        #
        sports_list = self.driver.find_elements(By.CLASS_NAME, "android.widget.TextView")
        sport = random.choice(sports_list)
        self.driver.find_element(By.XPATH, f'//android.widget.TextView[@text="{sport.text}"]').click()

        self.free_input.set_text(free)
        self.save_btn.click()
        return group
    
    def verify_add_succesfully(self, group) -> bool:
        return bool(self.toaster_succesfully_saved) and self.driver.find_element(By.XPATH, "//android.widget.TextView[@resource-id=\"groupNameText\"]").text == group