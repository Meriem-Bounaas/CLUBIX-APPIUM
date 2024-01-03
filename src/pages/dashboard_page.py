from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from lib.customLib import *

from src.pages.base.base_page import BasePage


class DashboardPage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver = driver

    locators = {
        "menu_burger" : ('xpath', '//android.widget.ImageView'),
    }

    def verify_page(self, langue) -> bool:
        if (langue == 'Fr'):
            return bool(self.driver.find_element(By.XPATH, "//android.view.View[@text=\"Tableau De Bord\"]"))
        if (langue == 'Ar'):
            return bool(self.driver.find_element(By.XPATH, "//android.view.View[@text=\"لوحة المعلومات\"]"))
        if (langue == 'En'):
            return bool(self.driver.find_element(By.XPATH, "//android.view.View[@text=\"Dashboard\"]"))
        
    
    def go_to_menu_burger(self) -> None:
        self.menu_burger.click()
    
    def go_to_logout_page(self, langue) -> None:
        self.go_to_menu_burger()
        if (langue == 'Fr'):
            self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"Déconnexion\"]").click()
        if (langue == 'Ar'):
            self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"تسجيل الخروج\"]").click()
        if (langue == 'En'):
            self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"Logout\"]").click()
    
    def go_to_sports_page(self, langue) -> None:
        self.go_to_menu_burger()
        if (langue == 'Fr'):
            self.driver.find_element(By.XPATH, "(//android.widget.TextView[@text=\"Mes Sports\"])[2]").click()
        if (langue == 'Ar'):
            self.driver.find_element(By.XPATH, "(//android.widget.TextView[@text=\"الرياضات\"])[2]").click()
        if (langue == 'En'):
            self.driver.find_element(By.XPATH, "(//android.widget.TextView[@text=\"My Sports\"])[2]").click()
    
    def go_to_groups_page(self, langue) -> None:
        self.go_to_menu_burger()
        if (langue == 'Fr'):
            self.driver.find_element(By.XPATH, "(//android.widget.TextView[@text=\"Mes Groupes\"])[2]").click()
        if (langue == 'Ar'):
            self.driver.find_element(By.XPATH, "(//android.widget.TextView[@text=\"مجموعاتي\"])[2]").click()
        if (langue == 'En'):
            self.driver.find_element(By.XPATH, "(//android.widget.TextView[@text=\"My Groups\"])[2]").click()
    
    def go_to_members_page(self, langue) -> None:
        if (langue == 'Fr'):
            self.driver.find_element(By.XPATH, "(//android.widget.TextView[@text=\"Membres\"])[2]").click()
        if (langue == 'Ar'):
            self.driver.find_element(By.XPATH, "(//android.widget.TextView[@text=\"الأعضاء\"])[2]").click()
        if (langue == 'En'):
            self.driver.find_element(By.XPATH, "(//android.widget.TextView[@text=\"Members\"])[2]").click()