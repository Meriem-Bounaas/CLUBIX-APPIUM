from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from lib.customLib import *

from src.pages.base.base_page import BasePage


class MembersPage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver = driver

    locators = {
        "add_btn" : ('xpath', '//*[@resource-id="addBtn"]'),
        "joining_date" : ('xpath', '//*[@resource-id="calendar1OpenBtn"]'),
        "confirm_date" : ('xpath', '//*[@resource-id="android:id/button1"]'),
        "birth_date" : ('xpath', '//*[@resource-id="Calendar2date"]'),
        "save_btn" : ('xpath', '//*[@resource-id="saveBtn"]'),
        "blood_type" : ('xpath', '//android.widget.TextView[@text="RH (O+,AB-, ...)?"]'),
        "first_name_input" : ('xpath', '//*[@resource-id="firstNameTextInput"]'),
        "last_name_input" : ('xpath', '//*[@resource-id="lastNameTextInput"]'),
        "phone_number_input" : ('xpath', '//*[@resource-id="phoneTextInput"]'),
        "toaster_succesfully_saved" : ('xpath', '//android.view.ViewGroup[@content-desc="succesfully saved"]'),
        "year_2025" : ('xpath', '//android.widget.Button[@text="2025"]'),
        "year_2023" : ('xpath', '//android.widget.Button[@text="2023"]'),
        "year_2021" : ('xpath', '//android.widget.Button[@text="2021"]'),
        "year_2019" : ('xpath', '//android.widget.Button[@text="2019"]'),
        "month_december" : ('xpath', '//android.widget.Button[@text="December"]'),
        "month_february" : ('xpath', '//android.widget.Button[@text="February"]'),
    }

    def verify_page(self, langue) -> bool:
        ''' function to verify the header of member's page'''
        if (langue == 'Fr'):
            return bool(self.driver.find_element(By.XPATH, "//android.view.View[@text=\"Membres\"]"))
        if (langue == 'Ar'):
            return bool(self.driver.find_element(By.XPATH, "//android.view.View[@text=\"الأعضاء\"]"))
        if (langue == 'En'):
            return bool(self.driver.find_element(By.XPATH, "//android.view.View[@text=\"Members\"]"))
    
    def verify_header_add_member(self, langue) -> bool:
        ''' function to verify the header of add member's page'''
        if (langue == 'Fr'):
            return bool(self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"Ajouter un Membre\"]"))
        if (langue == 'Ar'):
            return bool(self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"إضافة عضو\"]"))
        if (langue == 'En'):
            return bool(self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"Add a Member\"]"))
        
    def click_add_group(self, langue) -> None:
        ''' function to click add group button'''
        if (langue == 'Fr'):
            self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"+ groupe\"]").click()
        if (langue == 'Ar'):
            self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"+ مجموعة\"]").click()
        if (langue == 'En'):
            self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"+ Group\"]").click()
    
    def verify_add_succesfully(self) -> bool:
        ''' function to verify the succuss of save'''
        member_information = read_from_csv_file('members.csv')
        first_name = member_information[0]
        last_name = member_information[1]

        return bool(self.toaster_succesfully_saved) and bool(self.driver.find_element(By.XPATH, f"//android.widget.TextView[@text=\"{first_name} {last_name}\"]"))
    
    def select_group(self, langue) -> None:
        '''Function to select a group from the dropdown element'''
        if (langue == 'Fr'):
            self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"Sélectionner le Groupe\"]").click()
        if (langue == 'Ar'):
            self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"اختر المجموعة\"]").click()
        if (langue == 'En'):
            self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"Select the Group\"]").click()
    
    def fill_form(self, langue) -> None:
        '''Function to fill form and save informations in csv file'''
        first_name = generate_first_name()
        last_name = generate_last_name()
        phone_number = generate_phone_number()

        self.first_name_input.set_text(first_name)
        self.last_name_input.set_text(last_name)
        self.phone_number_input.set_text(phone_number)
        
        self.driver.scroll(self.phone_number_input, self.first_name_input)
        
        self.select_group(langue)
        group = read_from_csv_file('groups.csv')
        group_element = self.driver.find_element(By.XPATH, f"//android.view.ViewGroup[@content-desc=\"{group[0]}\"]")
        group_element.click()

        self.joining_date.click()
        self.confirm_date.click()

        self.driver.scroll(self.joining_date, self.first_name_input)
        self.driver.scroll(self.blood_type, self.joining_date)

        self.blood_type.click()
        rh_type_list = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-']
        rh_type = random.choice(rh_type_list)
        self.driver.find_element(By.XPATH, f'//android.widget.TextView[@text="{rh_type}"]').click()
        
        self.birth_date.click()
        self.driver.scroll(self.year_2023, self.year_2025)
        self.driver.scroll(self.year_2021, self.year_2023)
        self.driver.scroll(self.year_2019, self.year_2021)
        self.driver.scroll(self.month_december, self.month_february)
        self.confirm_date.click()

        save_in_csv_file('members.csv', ['first_name', 'last_name', 'phone_number', 'group', 'blood_type' ], [first_name, last_name, phone_number, group[0], rh_type])

    def add_member(self, langue) -> None:
        '''Function to add a member'''
        self.add_btn.click()
        self.verify_header_add_member(langue)
        self.fill_form(langue)
        self.save_btn.click()

    def go_to_dashboard_page(self, langue) -> None:
        ''' Function to navigate to the dashboard page'''
        if (langue == 'Fr'):
            self.driver.find_element(By.XPATH, "//android.view.View[@content-desc=\"Tableau de Bord\"]/android.view.ViewGroup").click()
        if (langue == 'Ar'):
            self.driver.find_element(By.XPATH, "//android.view.View[@content-desc=\"لوحة المعلومات\"]/android.view.ViewGroup").click()
        if (langue == 'En'):
            self.driver.find_element(By.XPATH, "//android.view.View[@content-desc=\"Dashboard\"]/android.view.ViewGroup").click()