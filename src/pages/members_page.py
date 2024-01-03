from selenium.webdriver.common.action_chains import ActionChains
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
        "name_group_input" : ('xpath', '//*[@resource-id="nameTextInput"]'),
        "free_input" : ('xpath', '//*[@resource-id="feesTextInput"]'),
        "submit_btn" : ('xpath', '//*[@resource-id="submitBtn"]'),
        "first_name_input" : ('xpath', '//*[@resource-id="firstNameTextInput"]'),
        "last_name_input" : ('xpath', '//*[@resource-id="lastNameTextInput"]'),
        "phone_number_input" : ('xpath', '//*[@resource-id="phoneTextInput"]'),
        "toaster_succesfully_saved" : ('xpath', '//android.view.ViewGroup[@content-desc="succesfully saved"]'),
    }

    def verify_page(self, langue) -> bool:
        if (langue == 'Fr'):
            return bool(self.driver.find_element(By.XPATH, "//android.view.View[@text=\"Membres\"]"))
        if (langue == 'Ar'):
            return bool(self.driver.find_element(By.XPATH, "//android.view.View[@text=\"الأعضاء\"]"))
        if (langue == 'En'):
            return bool(self.driver.find_element(By.XPATH, "//android.view.View[@text=\"Members\"]"))
    
    def verify_header_add_group(self, langue) -> bool:
        if (langue == 'Fr'):
            return bool(self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"Ajouter un Groupe\"]"))
        if (langue == 'Ar'):
            return bool(self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"إضافة مجموعة\"]"))
        if (langue == 'En'):
            return bool(self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"Add a Group\"]"))
    
    def verify_header_add_member(self, langue) -> bool:
        if (langue == 'Fr'):
            return bool(self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"Ajouter un Membre\"]"))
        if (langue == 'Ar'):
            return bool(self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"إضافة عضو\"]"))
        if (langue == 'En'):
            return bool(self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"Add a Member\"]"))
    
    def select_sport(self, langue):
        if (langue == 'Fr'):
            return self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"Quel Sport ?\"]")
        if (langue == 'Ar'):
            return self.driver.find_element(By.XPATH, "//android.widget.TextView[@text='أي نوع من الرياضة؟']")
        if (langue == 'En'):
            return self.driver.find_element(By.XPATH, "//android.widget.TextView[@text='Which Sport?']")
        
    def click_add_group(self, langue) -> None:
        if (langue == 'Fr'):
            self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"+ groupe\"]").click()
        if (langue == 'Ar'):
            self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"+ مجموعة\"]").click()
        if (langue == 'En'):
            self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"+ Group\"]").click()

    def add_group(self, langue) -> str:
        groups_list = ['femme_A1' , 'femme_A2', 'Homme_A1', 'Homme_A2', 'Enfant_A1', 'Enfant_A2']
        group = random.choice(groups_list)
        free = random.randint(50, 200)
        self.click_add_group(langue)
        self.verify_header_add_group(langue)
        self.name_group_input.set_text(group)
        select_sport_element = self.select_sport(langue)
        select_sport_element.click()
    
        sport = read_from_csv_file('sports.csv')
        sport_element = self.driver.find_element(By.XPATH, f"//android.view.ViewGroup[@content-desc=\"{sport[0]}\"]")
        sport_element.click()
        

        self.free_input.set_text(free)
        self.submit_btn.click()

        save_in_csv_file('groups.csv', ['group'], [group])
    
    def verify_add_succesfully(self) -> bool:
        member_information = read_from_csv_file('members.csv')
        first_name = member_information[0]
        last_name = member_information[1]

        return bool(self.toaster_succesfully_saved) and bool(self.driver.find_element(By.XPATH, f"//android.widget.TextView[@text=\"{first_name} {last_name}\"]"))
    
    def select_group(self, langue) -> None:
        if (langue == 'Fr'):
            self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"Sélectionner le Groupe\"]").click()
        if (langue == 'Ar'):
            self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"اختر المجموعة\"]").click()
        if (langue == 'En'):
            self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"Select the Group\"]").click()
    
    def fill_form(self, langue) -> None:
        first_name = generate_first_name()
        last_name = generate_last_name()
        phone_number = generate_phone_number()

        self.first_name_input.set_text(first_name)
        self.last_name_input.set_text(last_name)
        self.phone_number_input.set_text(phone_number)
        
        ActionChains(self.driver).scroll_to_element(self.phone_number_input)
        
        self.select_group(langue)
        group = read_from_csv_file('groups.csv')
        group_element = self.driver.find_element(By.XPATH, f"//android.view.ViewGroup[@content-desc=\"{group[0]}\"]")
        group_element.click()

        self.joining_date.click()
        self.confirm_date.click()

        self.blood_type.click()
        rh_type_list = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-']
        rh_type = random.choice(rh_type_list)
        self.driver.find_element(By.XPATH, f'//android.widget.TextView[@text="{rh_type}"]').click()

        self.birth_date.click()
        self.confirm_date.click()

        save_in_csv_file('members.csv', ['first_name', 'last_name', 'phone_number', 'group', 'blood_type' ], [first_name, last_name, phone_number, group[0], rh_type])

    def add_member(self, langue) -> None:
        self.add_btn.click()
        self.verify_header_add_member(langue)
        self.fill_form(langue)
        self.save_btn.click()