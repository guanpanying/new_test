import os

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities


class Base1:
    def setup(self):
        browser = os.getenv('browser')
        if browser == 'chrome':
            self.driver = webdriver.Chrome()

            desired_capabilities = DesiredCapabilities.CHROME
            desired_capabilities['pageLoadStrategy'] = 'none'
        elif browser == 'aa':
            self.driver = webdriver.PhantomJS('/Users/guanpy/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs')  # 无界面的浏览器

        else:
            self.driver = webdriver.Chrome()

        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()
