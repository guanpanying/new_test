from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.remote.mobile import Mobile

from app.pageobject2.page.base import BasePage
from app.pageobject2.page.edituserinfo_page import EditUserInfoPage


class MyTabPage(BasePage):
    # _login_button=(MobileBy.XPATH,'')

    def click_login(self):
        #点击登录
        # self.driver.find_element(MobileBy,'')

        from app.pageobject2.page.edituserinfo_page import EditUserInfoPage
        return EditUserInfoPage(self.driver)


    def verify_login_toast(self):
        # result=self.get_toast_text()
        return True

    def click_register(self):
        return True