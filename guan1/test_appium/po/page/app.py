from appium import webdriver

from test_appium.po.page.base import Base
from test_appium.po.page.main import Main


class App(Base):
    def start(self):
        if self.driver is None:
            caps = {}
            caps['platformName'] = 'android'
            caps['deviceName'] = 'emulator-5554'
            caps['appPackage'] = 'com.android.chrome'
            caps['appActivity'] = 'com.google.android.apps.chrome.Main'
            caps['noReset'] = 'true'
            caps['ensureWebviewsHavePages'] = 'true'
            caps['settings[waitForIdleTimeout]'] = 0
            caps['avd'] = 'Nexus_6_API_30'

            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
        else:
            self.driver.launch_app()
            """Start on the device the application specified in the desired capabilities.   """
        self.driver.implicitly_wait(7)

    def goto_main(self):

        return Main(self.driver)
