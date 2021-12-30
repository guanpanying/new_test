from time import sleep

import yaml
from selenium import webdriver


class TestFyong:
    def test_demo(self):
        option = webdriver.ChromeOptions()
        option.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=option)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')

        # self.driver.find_element_by_id()


def test_get_cookie():
    option = webdriver.ChromeOptions()
    option.debugger_address = '127.0.0.1:9222'
    driver = webdriver.Chrome(options=option)
    driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
    cookie = driver.get_cookies()
    with open('../test_web_weixin/page/data.yaml', 'w') as f:
        yaml.dump(cookie, f)


def test_login():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx')
    with open('../test_web_weixin/page/data.yaml') as f:
        yaml_data = yaml.safe_load(f)
        for i in yaml_data:
            driver.add_cookie(i)
    driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
    sleep(2)
