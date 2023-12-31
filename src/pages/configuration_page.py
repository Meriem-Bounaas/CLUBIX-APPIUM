from appium.webdriver.webdriver import WebDriver
from lib.customLib import *
from selenium.webdriver.common.by import By

from src.pages.base.base_page import BasePage


class ConfigurationPage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver = driver

    locators = {
        "title_langue_page": ('xpath', '//*[@resource-id="onboardTitle"]'),
        "toaster_succesfully_loged_in": ('xpath', '//android.widget.TextView[@text="succesfully loged in"]'),
        "langue_drop_down": ('xpath', '//android.widget.TextView[@text="FR"]'),
        "arrow_btn": ('xpath', '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]'),
        "first_name_input": ('xpath', '//*[@resource-id="firstNameTextInput"]'),
        "last_name_input": ('xpath', '//*[@resource-id="lastNameTextInput"]'),
        "submit_btn": ('xpath', '//*[@resource-id="submitBtn"]'),
        "bienvenue_username": ('xpath', '//*[@resource-id="OnboardScreenTitleText"]'),
        "next_btn": ('xpath', '//*[@resource-id="NextBtnTitle"]'),
        "club_name_input": ('xpath', '//*[@resource-id="nameTextInput"]'),
        "save_club_name_btn": ('xpath', '//*[@resource-id="saveBtn"]'),
        "upload_logo_btn": ('xpath', '//android.view.ViewGroup[@resource-id="selectImageBtn"]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView'),
        "header_sports_page": ('xpath', '//*[@resource-id="sportnamescreenTitle"]'),
    }

    def verify_page(self) -> bool:
        '''Function to verify the header of the salutation page'''
        return self.title_langue_page.text == "Salut"
    
    def succesfully_loged_in(self) -> bool:
        '''Function to verify the succuss of log in'''
        return bool(self.toaster_succesfully_loged_in)
    
    def add_langue(self) -> str:
        '''Function to add the preferred language'''
        self.langue_drop_down.click()
        langue = random.choice(['Fr', 'Ar', 'En'])
        langue_btn = self.driver.find_element(By.XPATH, f'//android.widget.TextView[@text="{langue}"]')
        langue_btn.click()
        return langue

    def verify_langue_page(self, langue) -> bool:
        ''' Function to verify the language of page'''
        return self.pages['configuration'][langue]['verify_langue_page'](self)
        
    def go_to_username_page(self) -> None:
        ''' Function to navigate to username page'''
        self.arrow_btn.click()

    def verify_username_page(self, langue) -> bool:
        ''' Function to verify the header of username page'''
        return self.pages['configuration'][langue]['verify_username_page'](self)

    def add_username(self) -> None:
        ''' Function to add the username'''
        username = generate_username()
        first_name = username.split(' ')[0]
        last_name = username.split(' ')[1]

        self.first_name_input.set_text(first_name)
        self.last_name_input.set_text(last_name)
        self.submit_btn.click()

        save_in_csv_file('username.csv', ['first_name', 'last_name'], [first_name, last_name])
    
    def succesfull_configuration(self, langue) -> bool:
        ''' Function to verify the succuss of configuration'''
        username = read_from_csv_file('username.csv')
        return self.pages['configuration'][langue]['succesfull_configuration'](self, username)
    
    def go_to_club_name_page(self) -> None:
        ''' Function to navigate to club name page'''
        self.next_btn.click()
    
    def verify_club_name_page(self, langue) -> bool:
        ''' Function to verify the header of club name page'''
        return self.pages['configuration'][langue]['verify_club_name_page'](self)

    def add_club_name(self) -> None:
        ''' Function to add a club name'''
        club_name = generate_club_name()
        self.club_name_input.set_text(club_name)
        self.save_club_name_btn.click()
    
    def verify_logo_club_page(self, langue) -> bool:
        ''' Function to verify the header of club's logo page'''
        return self.pages['configuration'][langue]['verify_logo_club_page'](self)

    def add_logo_club(self) -> None:
        ''' Function to add logo club'''
        # self.upload_logo_btn.click()
        # upload from mobile
        self.submit_btn.click()

    def verify_sport_page(self, langue) -> bool:
        ''' Function to verify the header of sports page'''
        return self.pages['configuration'][langue]['verify_sport_page'](self)
        
    def add_sports(self) -> None:
        ''' Function to add sport and save it in csv file'''
        sports_element = self.driver.find_elements(By.CLASS_NAME, 'android.widget.TextView')
        sport_element = random.choice(sports_element)
        sport_element.click()
        self.submit_btn.click()
        save_in_csv_file('sports.csv', ['sport'], [sport_element.text])
