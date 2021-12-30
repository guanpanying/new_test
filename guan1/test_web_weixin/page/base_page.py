import os

import yaml
from selenium import webdriver


class BasePage:
    def __init__(self, base_driver=None):
        if base_driver is None:
            self.driver = webdriver.Chrome()
            self.__cookie_login()
            self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
            self.driver.maximize_window()
            self.driver.implicitly_wait(5)
        else:
            self.driver = base_driver
        # self.__cookie_login()

    def __cookie_login(self):
        self.driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx')
        with open('/Users/guanpy/Desktop/guan1/test_web_weixin/page/data.yaml') as f:
            yaml_data = yaml.safe_load(f)
            for i in yaml_data:
                self.driver.add_cookie(i)
            # self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')

    def finds(self, by, value=None):
        if value == None:

            return self.driver.find_elements(*by)
        else:
            return self.driver.find_elements(by, value)

    def find(self, by, value=None):
        if value == None:
            return self.driver.find_element(*by)
        else:
            return self.driver.find_element(by, value)

    def quit(self):
        self.driver.quit()
