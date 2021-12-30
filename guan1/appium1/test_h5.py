from appium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class MobeileBy(object):
    pass


class TestH5:
    def setup(self):
        desired_cap = {
            'platformName': 'android',
            'platformVersion': '11',
            # 'browserName':'Chrome',
            'deviceName': 'emulator-5554',
            # 'noReset':True,
            # 'chromedriverExecutable':''
            'appPackage': 'com.google.android.apps.messaging',
            'appActivity': 'com.google.android.apps.messaging.ui.ConversationListActivity'
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_h(self):
        # self.driver.get('https://www.baidu.com/')
        print(self.driver.get_window_size())
        print(self.driver.get_window_rect())
        # self.driver.find_element_by_android_uiautomator(new UiSelector().text)
        # self.driver.find_element_by_android_uiautomator('new UiSelector().')  # 对应uiautomator名称：“text”
