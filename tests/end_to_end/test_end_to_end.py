from src.pages.registration_page import RegistrationPage
from src.pages.configuration_page import ConfigurationPage
from src.pages.login_page import LoginPage
from src.pages.dashboard_page import DashboardPage
from src.pages.members_page import MembersPage
from src.pages.logout_page import LogoutPage
from src.pages.sports_page import SportsPage

def test_end_to_end(login_page: LoginPage, registration_page: RegistrationPage, configuration_page: ConfigurationPage, dashboard_page: DashboardPage, members_page: MembersPage, logout_page: LogoutPage, sports_page: SportsPage):
    ''' Add member test successful'''

    assert login_page.verify_page()
    login_page.go_to_registration_page()
    assert registration_page.verify_page()
    registration_page.sign_up()
    assert registration_page.verify_toaster_successful_registration()
    assert login_page.verify_page()
    login_page.sign_in()
    assert configuration_page.succesfully_loged_in()
    assert configuration_page.verify_page()
    langue = configuration_page.add_langue()
    assert configuration_page.verify_langue_page(langue)
    configuration_page.go_to_username_page()
    assert configuration_page.verify_username_page(langue)
    configuration_page.add_username()
    assert configuration_page.succesfull_configuration(langue)
    configuration_page.go_to_club_name_page()
    assert configuration_page.verify_club_name_page(langue)
    configuration_page.add_club_name()
    assert configuration_page.verify_logo_club_page(langue)
    configuration_page.add_logo_club()
    assert configuration_page.verify_sport_page(langue)
    configuration_page.add_sports()
    assert dashboard_page.verify_page(langue)
    dashboard_page.go_to_sports_page(langue)
    assert sports_page.verify_page(langue)
    sports_page.add_sport(langue)
    assert sports_page.verify_add_succesfully()
    dashboard_page.go_to_dashboard_page(langue)
    dashboard_page.go_to_members_page(langue)
    assert members_page.verify_page(langue)
    members_page.add_group(langue)
    members_page.add_member(langue)
    assert members_page.verify_add_succesfully()
    members_page.go_to_dashboard_page(langue)
    dashboard_page.go_to_logout_page(langue)
    assert logout_page.verify_page(langue)
    logout_page.logout()
    assert login_page.verify_page()