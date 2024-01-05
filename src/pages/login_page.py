from appium.webdriver.webdriver import WebDriver
from lib.customLib import *

from src.pages.base.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver = driver

    locators = {
        "login_page_title" : ('xpath', '//*[@resource-id="LoginText"]'),
        "email_input": ('XPATH', '//*[@resource-id="emailTextInput"]'),
        "password_input": ('XPATH', '//*[@resource-id="passwordTextInput"]'),
        "submit_btn": ('XPATH', '//*[@resource-id="ConnexionBtn"]'),
        "registration_btn": ('xpath', '//*[@resource-id="RegistrationBtn"]'),        
    }

    def verify_page(self) -> bool:
        ''' function to verify the header of login page'''
        return bool(self.login_page_title)
    
    def go_to_registration_page(self) -> None:
        ''' Function to navigate to the registration page'''
        self.registration_btn.click()
    
    def sign_in(self) -> None:
        ''' Function to sign in'''
        login_data = read_from_csv_file('registration.csv')

        self.email_input.set_text(login_data[0])
        self.password_input.set_text(login_data[1])
        self.submit_btn.click()