from appium.webdriver.webdriver import WebDriver
from seleniumpagefactory.Pagefactory import PageFactory


class BasePage(PageFactory):
    def __init__(self, driver: WebDriver) -> None:
        super().__init__()
        self.driver = driver
    locators ={}