from appium import webdriver

from app.pageobject1.page.main_page import MainPage


class App:
    def start(self):
        # caps = {}
        # caps['udid'] = 'udid'
        # caps['deviceName'] = 'udid'
        # caps['platform'] = 'android'
        # caps['noReset'] = 'true'
        # caps['appPackage'] = 'com.android.settings'
        # caps['appActivity'] = 'com.android.settings.homepage.SettingsHomepageActivity'
        #
        # self.driver = webdriver.Remote('http://127.0.0.1:4723' + '/wd/hub', caps)
        # self.driver.implicitly_wait(5)
        return self

    def stop(self):
        pass

    def restart(self):
        pass

    def goto_main(self):
        #入口，从APP启动后进入首页
        return MainPage()