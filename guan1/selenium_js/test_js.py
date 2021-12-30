import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from selenium_js.base import Base1
import time


class TestJs(Base1):
    def test_js(self):
        self.driver.get('https://www.baidu.com')

        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of(self.driver.find_element_by_id('kw')))
        self.driver.find_element_by_id('kw').send_keys('测试')

        self.driver.execute_script('return document.getElementById("su")').click()
        print(self.driver.execute_script('return JSON.stringify(performance.timing)'))

        time.sleep(3)


if __name__ == '__main__':
    for i in range(10):
        pytest.main(['-v', '-s', 'test_js.py'])
        print(i)
