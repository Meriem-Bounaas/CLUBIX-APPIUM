from src.pages.registration_page import RegistrationPage
from src.pages.configuration_page import ConfigurationPage
from src.pages.login_page import LoginPage
from src.pages.dashboard_page import DashboardPage
from src.pages.groups_page import GroupsPage

def test_add_group(login_page: LoginPage, registration_page: RegistrationPage, configuration_page: ConfigurationPage, dashboard_page: DashboardPage, groups_page: GroupsPage):
    ''' Add group test successful'''

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
    dashboard_page.go_to_groups_page(langue)
    assert groups_page.verify_page(langue)
    group = groups_page.add_group(langue)
    assert groups_page.verify_add_succesfully(group)