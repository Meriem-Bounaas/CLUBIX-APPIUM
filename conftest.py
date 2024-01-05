import logging
import allure
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.webdriver import WebDriver

from src.pages.login_page import LoginPage
from src.pages.registration_page import RegistrationPage
from src.pages.configuration_page import ConfigurationPage
from src.pages.dashboard_page import DashboardPage
from src.pages.sports_page import SportsPage
from src.pages.logout_page import LogoutPage
from src.pages.groups_page import GroupsPage
from src.pages.members_page import MembersPage


APPIUM_HOST = '127.0.0.1'
APPIUM_PORT = 4723
APPIUM_PATH = '/wd/hub'

@pytest.fixture(scope="session")
def start_appium_server():
    service = AppiumService()
    service.start(
        args=['--address', APPIUM_HOST,
              '-p', str(APPIUM_PORT),
              '-pa', APPIUM_PATH],
        timeout_ms=300000,
    )

    while not service.is_running:
        logging.info('starting server')

    yield service

    service.stop()

@pytest.fixture()
def driver():
    options = UiAutomator2Options()
    options.automation_name = 'UiAutomator2'
    options.platform_name = "Android"
    options.app = "C:/Users/a914710/VsCodeProjects/clubix-test/src/app/app-release.apk"
    options.avd = "Pixel_2_API_34"
    options.avd_launch_timeout = 30000
    
    driver = webdriver.Remote(
        f"http://{APPIUM_HOST}:{APPIUM_PORT}{APPIUM_PATH}", options=options)
    driver.implicitly_wait(10)

    yield driver

    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call) -> None:
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        if 'browser' in item.fixturenames:
            web_driver = item.funcargs['browser']
        else:
            print('Failed to find web driver')
            return

        # Attach a screenshot if a test failed
        allure.attach(
            web_driver.get_screenshot_as_png(),
            name='screenshot',
            attachment_type=allure.attachment_type.PNG
        )

@pytest.fixture()
def login_page(driver: WebDriver) -> LoginPage:
    login = LoginPage(driver)
    yield login

@pytest.fixture()
def registration_page(driver: WebDriver) -> RegistrationPage:
    registration = RegistrationPage(driver)
    yield registration

@pytest.fixture()
def configuration_page(driver: WebDriver) -> ConfigurationPage:
    langue = ConfigurationPage(driver)
    yield langue

@pytest.fixture()
def dashboard_page(driver: WebDriver) -> DashboardPage:
    dashboard = DashboardPage(driver)
    yield dashboard

@pytest.fixture()
def sports_page(driver: WebDriver) -> SportsPage:
    sport = SportsPage(driver)
    yield sport

@pytest.fixture()
def logout_page(driver: WebDriver) -> LogoutPage:
    logout = LogoutPage(driver)
    yield logout

@pytest.fixture()
def groups_page(driver: WebDriver) -> GroupsPage:
    group = GroupsPage(driver)
    yield group

@pytest.fixture()
def members_page(driver: WebDriver) -> MembersPage:
    member = MembersPage(driver)
    yield member