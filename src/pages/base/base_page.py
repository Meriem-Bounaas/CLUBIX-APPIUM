from appium.webdriver.webdriver import WebDriver
from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.common.by import By
from lib.customLib import *


class BasePage(PageFactory):
    def __init__(self, driver: WebDriver) -> None:
        super().__init__()
        self.driver = driver
        
    locators ={
    }

    pages = {
    'configuration': {
        'Fr': {
            'verify_langue_page': lambda self: self.title_langue_page.text == 'Salut',
            'verify_username_page': lambda self: bool(self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"Votre Nom complet S'il Vous Plaît!\"]")),
            'succesfull_configuration': lambda self, username: self.bienvenue_username.text == f'Salut, {username[0]} {username[1]}',
            'verify_club_name_page':  lambda self: bool(self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"Nom de Votre Club?\"]")),
            'verify_logo_club_page': lambda self: bool(self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"Télécharger le logo du club ?\"]")),
            'verify_sport_page': lambda self: self.header_sports_page.text == 'Quel Sport ?'

        },
        'Ar': {
            'verify_langue_page': lambda self: self.title_langue_page.text == 'مرحبًا',
            'verify_username_page': lambda self: bool(self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"اسمك الكامل من فضلك!\"]")),
            'succesfull_configuration': lambda self, username: self.bienvenue_username.text == f'مرحبًا, {username[0]} {username[1]}',
            'verify_club_name_page':  lambda self: bool(self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"اسم ناديك؟\"]")),
            'verify_logo_club_page': lambda self: bool(self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"تحميل شعار النادي؟\"]")),
            'verify_sport_page': lambda self: self.header_sports_page.text == 'أي نوع من الرياضة؟'

        },
        'En': {
            'verify_langue_page':  lambda self:  self.title_langue_page.text == 'Hi',
            'verify_username_page': lambda self: bool(self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"Your Full Name Please!\"]")),
            'succesfull_configuration': lambda self, username: self.bienvenue_username.text == f'Hi, {username[0]} {username[1]}',
            'verify_club_name_page':  lambda self:  bool(self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"Your Club's Name?\"]")),
            'verify_logo_club_page': lambda self: bool(self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"Upload the club logo?\"]")),
            'verify_sport_page': lambda self: self.header_sports_page.text == 'Which Sport?'

        }
    },
    'dashboard': {
        'Fr': {
            'verify_page': lambda self: bool(self.driver.find_element(By.XPATH, "//android.view.View[@text=\"Tableau De Bord\"]")),
            'go_to_logout_page': lambda self: self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"Déconnexion\"]").click(),
            'go_to_sports_page': lambda self: self.driver.find_element(By.XPATH, "(//android.widget.TextView[@text=\"Mes Sports\"])[2]").click(),
            'go_to_groups_page':  lambda self: self.driver.find_element(By.XPATH, "(//android.widget.TextView[@text=\"Mes Groupes\"])[2]").click(),
            'go_to_members_page': lambda self: self.driver.find_element(By.XPATH, "(//android.widget.TextView[@text=\"Membres\"])[2]").click()
        },
        'Ar': {
            'verify_page': lambda self: bool(self.driver.find_element(By.XPATH, "//android.view.View[@text=\"لوحة المعلومات\"]")),
            'go_to_logout_page': lambda self: self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"تسجيل الخروج\"]").click(),
            'go_to_sports_page': lambda self: self.driver.find_element(By.XPATH, "(//android.widget.TextView[@text=\"الرياضات\"])[2]").click(),
            'go_to_groups_page':  lambda self: self.driver.find_element(By.XPATH, "(//android.widget.TextView[@text=\"مجموعاتي\"])[2]").click(),
            'go_to_members_page': lambda self: self.driver.find_element(By.XPATH, "(//android.widget.TextView[@text=\"الأعضاء\"])[2]").click()
        },
        'En': {
            'verify_page': lambda self: bool(self.driver.find_element(By.XPATH, "//android.view.View[@text=\"Dashboard\"]")),
            'go_to_logout_page': lambda self: self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"Logout\"]").click(),
            'go_to_sports_page': lambda self: self.driver.find_element(By.XPATH, "(//android.widget.TextView[@text=\"My Sports\"])[2]").click(),
            'go_to_groups_page':  lambda self: self.driver.find_element(By.XPATH, "(//android.widget.TextView[@text=\"My Groups\"])[2]").click(),
            'go_to_members_page': lambda self: self.driver.find_element(By.XPATH, "(//android.widget.TextView[@text=\"Members\"])[2]").click()
        }
    },
    'members': {
        'Fr': {
            'verify_page': lambda self: bool(self.driver.find_element(By.XPATH, "//android.view.View[@text=\"Membres\"]")),
            'verify_header_add_member': lambda self: bool(self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"Ajouter un Membre\"]")),
            'click_add_group': lambda self: self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"+ groupe\"]").click(),
            'select_group':  lambda self: self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"Sélectionner le Groupe\"]").click(),
            'go_to_dashboard_page': lambda self: self.driver.find_element(By.XPATH, "//android.view.View[@content-desc=\"Tableau de Bord\"]/android.view.ViewGroup").click()
        },
        'Ar': {
            'verify_page': lambda self: bool(self.driver.find_element(By.XPATH, "//android.view.View[@text=\"الأعضاء\"]")),
            'verify_header_add_member': lambda self: bool(self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"إضافة عضو\"]")),
            'click_add_group': lambda self: self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"+ مجموعة\"]").click(),
            'select_group':  lambda self: self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"اختر المجموعة\"]").click(),
            'go_to_dashboard_page': lambda self: self.driver.find_element(By.XPATH, "(//android.widget.TextView[@text=\"الأعضاء\"])[2]").click()
        },
        'En': {
            'verify_page': lambda self: bool(self.driver.find_element(By.XPATH, "//android.view.View[@text=\"Members\"]")),
            'verify_header_add_member': lambda self: bool(self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"Add a Member\"]")),
            'click_add_group': lambda self: self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"+ Group\"]").click(),
            'select_group':  lambda self: self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"Select the Group\"]").click(),
            'go_to_dashboard_page': lambda self: self.driver.find_element(By.XPATH, "(//android.widget.TextView[@text=\"Members\"])[2]").click()
        }
    },
    'sports': {
        'Fr': {
            'verify_page': lambda self: bool(self.driver.find_element(By.XPATH, "//android.view.View[@text=\"Mes Sports\"]")),
            'verify_header_add_sport': lambda self: bool(self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"Ajouter un Sport\"]")),
            'go_to_dashboard_page': lambda self: self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"Tableau de bord\"]").click()
        },
        'Ar': {
            'verify_page': lambda self: bool(self.driver.find_element(By.XPATH, "//android.view.View[@text=\"الرياضات\"]")),
            'verify_header_add_sport': lambda self: bool(self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"إضافة رياضة\"]")),
            'go_to_dashboard_page': lambda self: self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"لوحة المعلومات\"]").click()
        },
        'En': {
            'verify_page': lambda self: bool(self.driver.find_element(By.XPATH, "//android.view.View[@text=\"My Sports\"]")),
            'verify_header_add_sport': lambda self: bool(self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"Add a Sport\"]")),
            'go_to_dashboard_page': lambda self: self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"Dashboard\"]").click()
        }
    },
    'groups': {
        'Fr': {
            'verify_page': lambda self: bool(self.driver.find_element(By.XPATH, "//android.view.View[@text=\"Mes Groupes\"]"))
        },
        'Ar': {
            'verify_page': lambda self: bool(self.driver.find_element(By.XPATH, "//android.view.View[@text=\"مجموعاتي\"]"))
        },
        'En': {
            'verify_page': lambda self: bool(self.driver.find_element(By.XPATH, "//android.view.View[@text=\"My Groups\"]"))
        }
    },
    'logout': {
        'Fr': {
            'verify_page': lambda self: bool(self.driver.find_element(By.XPATH, "//android.view.View[@text=\"Déconnexion\"]"))
        },
        'Ar': {
            'verify_page': lambda self: bool(self.driver.find_element(By.XPATH, "//android.view.View[@text=\"تسجيل الخروج\"]"))
        },
        'En': {
            'verify_page': lambda self: bool(self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"Logout\"]"))
        }
    },
    }

    def select_sport(self, langue) -> None:
        if (langue == 'Fr'):
            return self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"Quel Sport ?\"]").click()
        if (langue == 'Ar'):
            return self.driver.find_element(By.XPATH, "//android.widget.TextView[@text='أي نوع من الرياضة؟']").click()
        if (langue == 'En'):
            return self.driver.find_element(By.XPATH, "//android.widget.TextView[@text='Which Sport?']").click()
          
    def verify_header_add_group(self, langue) -> bool:
        if (langue == 'Fr'):
            return bool(self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"Ajouter un Groupe\"]"))
        if (langue == 'Ar'):
            return bool(self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"إضافة مجموعة\"]"))
        if (langue == 'En'):
            return bool(self.driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"Add a Group\"]"))