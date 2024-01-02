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
        return self.title_langue_page.text == "Salut"
    
    def succesfully_loged_in(self) -> bool:
        return bool(self.toaster_succesfully_loged_in)
    
    def add_langue(self) -> str:
        self.langue_drop_down.click()
        langue = random.choice(['Fr', 'Ar', 'En'])
        langue_btn = self.driver.find_element(By.XPATH, f'//android.widget.TextView[@text="{langue}"]')
        langue_btn.click()
        return langue

    def verify_langue_page(self, langue) -> bool:
        if (langue == 'Fr'):
            return self.title_langue_page.text == 'Salut'
        if (langue == 'Ar'):
            return self.title_langue_page.text == 'مرحبًا'
        if (langue == 'En'):
            return self.title_langue_page.text == 'Hi'
        
    def go_to_username_page(self) -> None:
        self.arrow_btn.click()

    def verify_username_page(self, langue) -> bool:
        if (langue == 'Fr'):
            return bool(self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"Votre Nom complet S'il Vous Plaît!\"]"))
        if (langue == 'Ar'):
            return bool(self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"اسمك الكامل من فضلك!\"]"))
        if (langue == 'En'):
            return bool(self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"Your Full Name Please!\"]"))

    def add_username(self) -> None:
        username = generate_username()
        first_name = username.split(' ')[0]
        last_name = username.split(' ')[1]

        self.first_name_input.set_text(first_name)
        self.last_name_input.set_text(last_name)
        self.submit_btn.click()

        save_in_csv_file('username.csv', ['first_name', 'last_name'], [first_name, last_name])
    
    def succesfull_configuration(self, langue) -> bool:
        username = read_from_csv_file('username.csv')
        if (langue == 'Fr'):
            return self.bienvenue_username.text == f'Salut, {username[0]} {username[1]}'
        if (langue == 'Ar'):
            return self.bienvenue_username.text == f'مرحبًا, {username[0]} {username[1]}'
        if (langue == 'En'):
            return self.bienvenue_username.text == f'Hi, {username[0]} {username[1]}'
    
    def go_to_club_name_page(self) -> None:
        self.next_btn.click()
    
    def verify_club_name_page(self, langue) -> bool:
        if (langue == 'Fr'):
            return bool(self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"Nom de Votre Club?\"]"))
        if (langue == 'Ar'):
            return bool(self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"اسم ناديك؟\"]"))
        if (langue == 'En'):
            return bool(self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"Your Club's Name?\"]"))
    
    def add_club_name(self) -> None:
        club_name = generate_club_name()
        self.club_name_input.set_text(club_name)
        self.save_club_name_btn.click()
    
    def verify_logo_club_page(self, langue) -> bool:
        if (langue == 'Fr'):
            return bool(self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"Télécharger le logo du club ?\"]"))
        if (langue == 'Ar'):
            return bool(self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"تحميل شعار النادي؟\"]"))
        if (langue == 'En'):
            return bool(self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"Upload the club logo?\"]"))

    def add_logo_club(self) -> None:
        # self.upload_logo_btn.click()
        # upload from mobile
        self.submit_btn.click()

    def verify_sport_page(self, langue) -> bool:
        if (langue == 'Fr'):
            return self.header_sports_page.text == 'Quel Sport ?'
        if (langue == 'Ar'):
            return self.header_sports_page.text == 'أي نوع من الرياضة؟'
        if (langue == 'En'):
            return self.header_sports_page.text == 'Which Sport?'
        
    def add_sports(self) -> None:
        sports_element = self.driver.find_elements(By.CLASS_NAME, 'android.widget.TextView')
        sport_element = random.choice(sports_element)
        sport_element.click()
        self.submit_btn.click()
        save_in_csv_file('sports.csv', ['sport'], [sport_element.text])