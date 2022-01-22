from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from app.pageobject1.page.my_tab_page import MyTabPage


class MainPage():
    # def __init__(self,driver:WebDriver):
    #     self.driver=driver

    def goto_my_tab(self):
        #点击'我的'tab
        # self.driver.find_element(MobileBy.XPATH,'')
        return MyTabPage()


