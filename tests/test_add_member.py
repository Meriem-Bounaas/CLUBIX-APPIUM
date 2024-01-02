from src.pages.registration_page import RegistrationPage
from src.pages.configuration_page import ConfigurationPage
from src.pages.login_page import LoginPage
from src.pages.dashboard_page import DashboardPage
from src.pages.sports_page import SportsPage

def test_add_member(login_page: LoginPage, registration_page: RegistrationPage, configuration_page: ConfigurationPage, dashboard_page: DashboardPage, sports_page: SportsPage):
    ''' Add member test successful'''
 