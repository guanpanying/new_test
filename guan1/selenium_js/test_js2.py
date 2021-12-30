import time

from selenium_js.base import Base1


class TestJs2(Base1):
    def test_js2(self):
        self.driver.get('https://www.12306.cn/index/')

        self.driver.execute_script('a=document.getElementById("train_date");a.removeAttribute("readonly")')
        self.driver.execute_script('document.getElementById("train_date").value="2022"')
        time.sleep(3)
