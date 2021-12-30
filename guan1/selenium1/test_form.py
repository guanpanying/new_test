from time import sleep

from selenium import webdriver
from selenium.webdriver import TouchActions
from selenium.webdriver.common.by import By


class TestForm:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_form(self):
        self.driver.get('https://www.baidu.com')
        self.driver.find_element(By.LINK_TEXT, '登录').click()
        sleep(2)
        self.driver.find_element_by_id('TANGRAM__PSP_11__userName').send_keys('13463110998')
        sleep(2)
        self.driver.find_element_by_id('TANGRAM__PSP_11__password').send_keys('guan.419708')
        sleep(2)
        self.driver.find_element_by_id('TANGRAM__PSP_11__submit').click()
        sleep(2)
        print((self.driver.find_element_by_id('TANGRAM__PSP_11__error').text))
        aa = TouchActions(self.driver)

        sleep(3)
