from appium.webdriver.webdriver import WebDriver


class Base:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self):
        pass
