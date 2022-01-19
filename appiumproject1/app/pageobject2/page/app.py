import logging
import os

from appium import webdriver

from app.pageobject2.page.base import BasePage
from app.pageobject2.page.main_page import MainPage


class App(BasePage):
    def start(self):
        # self.udid=os.getenv('udid')
        # self.port=os.getenv('port')
        # if self.driver == None:

            # caps = {}
            # caps['udid'] = 'udid'
            # caps['deviceName'] = 'udid'
            # caps['platform'] = 'android'
            # caps['noReset'] = 'true'
            # caps['appPackage'] = 'com.android.settings'
            # caps['appActivity'] = 'com.android.settings.homepage.SettingsHomepageActivity'
            #
            # self.driver = webdriver.Remote(f'http://127.0.0.1:' + {self.udid}+ '/wd/hub', caps)
            # self.driver.implicitly_wait(5)
        # else:
        #     self.driver.launch_app()
            #self.driver.start_activity(包名，activity)
        return self

    def stop(self):
        pass

    def restart(self):
        logging.info('guan')
        pass

    def goto_main(self):
        #入口，从APP启动后进入首页
        return MainPage(self.driver)