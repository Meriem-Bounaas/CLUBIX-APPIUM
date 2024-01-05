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
        return self.pages['dashboard'][langue]['verify_page'](self)
    
    def go_to_menu_burger(self) -> None:
        '''Function to display the burger menu'''
        self.menu_burger.click()
    
    def go_to_logout_page(self, langue) -> None:
        ''' Function to navigate to the logout page'''
        self.go_to_menu_burger()
        return self.pages['dashboard'][langue]['go_to_logout_page'](self)
    
    def go_to_sports_page(self, langue) -> None:
        ''' Function to navigate to the sports page'''
        self.go_to_menu_burger()
        return self.pages['dashboard'][langue]['go_to_sports_page'](self)
    
    def go_to_groups_page(self, langue) -> None:
        ''' Function to navigate to the groups page'''
        self.go_to_menu_burger()
        return self.pages['dashboard'][langue]['go_to_groups_page'](self)
    
    def go_to_members_page(self, langue) -> None:
        ''' Function to navigate to the members page'''
        return self.pages['dashboard'][langue]['go_to_members_page'](self)