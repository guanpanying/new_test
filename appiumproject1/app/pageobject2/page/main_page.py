from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from app.pageobject2.page.base import BasePage
from app.pageobject2.page.my_tab_page import MyTabPage


class MainPage(BasePage):
    # _mytab_ele=(MobileBy.XPATH,'//*[]')

    def goto_my_tab(self):
        #点击'我的'tab
        # self.driver.find_element(*self._mytab_ele)
        return MyTabPage(self.driver)


