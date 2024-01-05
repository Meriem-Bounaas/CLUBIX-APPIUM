from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from lib.customLib import *

from src.pages.base.base_page import BasePage


class SportsPage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver = driver

    locators = {
        "menu_burger" : ('xpath', '//android.widget.ImageView'),
        "add_btn" : ('xpath', '//*[@resource-id="addBtn"]'),
        "name_sport_input" : ('xpath', '//*[@resource-id="nameTextInput"]'),
        "save_btn" : ('xpath', '//*[@resource-id="submitBtn"]'),
        "toaster_succesfully_saved" : ('xpath', '//android.view.ViewGroup[@content-desc="succesfully saved"]'),
    }

    def verify_page(self, langue) -> bool:
        ''' function to verify the header of sports page'''
        if (langue == 'Fr'):
            return bool(self.driver.find_element(By.XPATH, "//android.view.View[@text=\"Mes Sports\"]"))
        if (langue == 'Ar'):
            return bool(self.driver.find_element(By.XPATH, "//android.view.View[@text=\"الرياضات\"]"))
        if (langue == 'En'):
            return bool(self.driver.find_element(By.XPATH, "//android.view.View[@text=\"My Sports\"]"))
    
    def verify_header_add_sport(self, langue) -> bool:
        ''' function to verify the header of add a sport's page'''
        if (langue == 'Fr'):
            return bool(self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"Ajouter un Sport\"]"))
        if (langue == 'Ar'):
            return bool(self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"إضافة رياضة\"]"))
        if (langue == 'En'):
            return bool(self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"Add a Sport\"]"))

    def add_sport(self, langue) -> str:
        ''' function to add sport and save it in csv file'''
        sports_list = ['Football' , 'Basketball', 'Tennis', 'Cricket', 'Rugby', 'Golf', 'Natation', 'Volleyball', 'Baseball']
        sport = random.choice(sports_list)
        self.add_btn.click()
        self.verify_header_add_sport(langue)
        self.name_sport_input.set_text(sport)
        self.save_btn.click()
        save_in_csv_file('sports.csv', ['sport'], [sport])

    def go_to_menu_burger(self) -> None:
        '''Function to display the burger menu'''
        self.menu_burger.click()
    
    def go_to_dashboard_page(self, langue) -> None:
        ''' Function to navigate to the dashboard page'''
        self.go_to_menu_burger()
        if (langue == 'Fr'):
            self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"Tableau de bord\"]").click()
        if (langue == 'Ar'):
            self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"لوحة المعلومات\"]").click()
        if (langue == 'En'):
            self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"Dashboard\"]").click()
    
    def verify_add_succesfully(self) -> bool:
        ''' function to verify the succuss of save'''
        sport = read_from_csv_file('sports.csv')
        return bool(self.toaster_succesfully_saved) and bool(self.driver.find_element(By.XPATH, f"//android.widget.TextView[@text=\"{sport[0]}\"]"))