from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWait:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_xswait(self):
        self.driver.get('https://www.baidu.com')
        ele = self.driver.find_element_by_id('su')
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of(ele))
        print('success')
