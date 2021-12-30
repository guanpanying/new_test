import time

import yaml
from selenium import webdriver
from selenium.webdriver.support import expected_conditions


class TestCookie:
    def test_cookie(self):
        option = webdriver.ChromeOptions()
        option.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=option)

        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        cookie = self.driver.get_cookies()
        with open('../page/data.yaml', 'w', encoding='utf-8') as f:
            yaml.dump(cookie, f)

        # self.driver = webdriver.Chrome()
        # self.driver.implicitly_wait(3)
        #
        #
        # self.driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx')
        # with open('../page/data.yaml', encoding='utf-8') as f:
        #     cook=yaml.safe_load(f)
        #
        #     for k in cook:
        #         self.driver.add_cookie(k)
        # self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        # time.sleep(2)

    def test_login(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(3)
        driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx')
        with open('../test_web_weixin/page/data.yaml') as f:
            yaml_data = yaml.safe_load(f)
            for i in yaml_data:
                driver.add_cookie(i)
        driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        time.sleep(2)
