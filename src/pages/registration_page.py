from appium.webdriver.webdriver import WebDriver
from lib.customLib import *

from src.pages.base.base_page import BasePage

class RegistrationPage(BasePage):

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.driver = driver

    locators = {
        "email_input": ('xpath', '//*[@resource-id="emailTextInput"]'),
        "password_input": ('xpath', '//*[@resource-id="passwordTextInput"]'),
        "confirm_password_input": ('xpath', '//*[@resource-id="confirmPasswordTextInput"]'),
        "submit_btn": ('xpath', '//*[@resource-id="RegistrationBtnTitle"]'),

        "register_page_title" : ('XPATH', '//android.widget.TextView[@text="Inscription"][1]'),
        "server_error_message" : ('XPATH', '//*[@resource-id="serverError"]'),
        "toaster_succesfully": ('xpath', '//android.widget.TextView[@text="succesfully saved"]')
    }
    
    def verify_page(self) -> bool:
        ''' function to verify the title of register page'''
        return self.register_page_title.text == "Inscription"

    def sign_up(self) -> None:
        ''' function to sign up'''
        email = generate_email()
        password = generate_password()

        self.email_input.set_text(email)
        self.password_input.set_text(password)
        self.confirm_password_input.set_text(password)
        self.submit_btn.click()
        save_in_csv_file('registration.csv', ['email','password'], [email,password])
        
    def verify_toaster_successful_registration(self) -> bool:
        ''' function to verify the succuss of registration'''
        return self.toaster_succesfully.text == 'succesfully saved'