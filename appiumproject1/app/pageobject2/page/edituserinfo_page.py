from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from app.pageobject2.page.base import BasePage


class EditUserInfoPage(BasePage):
    # def __init__(self,driver:WebDriver):
    #     self.driver=driver

    def edit_contact(self):
        #输入手机号
        #万能验证码
        # 点击login
        # self.driver.find_element(MobileBy,'').send_keys('')
        from app.pageobject2.page.my_tab_page import MyTabPage

        return MyTabPage(self.driver)


