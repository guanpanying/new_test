from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.remote.mobile import Mobile

from app.pageobject1.page.edituserinfo_page import EditUserInfoPage


class MyTabPage:
    # def __init__(self,driver:WebDriver):
    #     self.driver=driver

    def click_login(self):
        #点击登录
        # self.driver.find_element(MobileBy,'')

        from app.pageobject1.page.edituserinfo_page import EditUserInfoPage
        return EditUserInfoPage()


    def verify_login_toast(self):
        # text=self.driver.find_element(MobileBy.XPATH,'//*[class="android.widget.Toast"]').get_attribute('text')
        return True

    def click_register(self):
        return True