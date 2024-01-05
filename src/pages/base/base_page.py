from appium.webdriver.webdriver import WebDriver
from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.common.by import By
from lib.customLib import *


class BasePage(PageFactory):
    def __init__(self, driver: WebDriver) -> None:
        super().__init__()
        self.driver = driver
    locators ={
        "add_btn" : ('xpath', '//*[@resource-id="addBtn"]'),
        "name_group_input" : ('xpath', '//*[@resource-id="nameTextInput"]'),
        "free_input" : ('xpath', '//*[@resource-id="feesTextInput"]'),
        "save_btn" : ('xpath', '//*[@resource-id="submitBtn"]'),
    }

    def select_sport(self, langue) -> None:
        if (langue == 'Fr'):
            return self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"Quel Sport ?\"]").click()
        if (langue == 'Ar'):
            return self.driver.find_element(By.XPATH, "//android.widget.TextView[@text='أي نوع من الرياضة؟']").click()
        if (langue == 'En'):
            return self.driver.find_element(By.XPATH, "//android.widget.TextView[@text='Which Sport?']").click()
          
    def add_group(self, langue) -> str:
        groups_list = ['femme_A1' , 'femme_A2', 'Homme_A1', 'Homme_A2', 'Enfant_A1', 'Enfant_A2']
        group = random.choice(groups_list)
        free = random.randint(50, 200)
        self.add_btn.click()
        self.verify_header_add_group(langue)
        self.name_group_input.set_text(group)
        self.select_sport(langue)
    
        sport = read_from_csv_file('sports.csv')
        sport_element = self.driver.find_element(By.XPATH, f"//android.view.ViewGroup[@content-desc=\"{sport[0]}\"]")
        sport_element.click()

        self.free_input.set_text(free)
        self.save_btn.click()

        save_in_csv_file('groups.csv', ['group'], [group])

    def verify_header_add_group(self, langue) -> bool:
        if (langue == 'Fr'):
            return bool(self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"Ajouter un Groupe\"]"))
        if (langue == 'Ar'):
            return bool(self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"إضافة مجموعة\"]"))
        if (langue == 'En'):
            return bool(self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"Add a Group\"]"))