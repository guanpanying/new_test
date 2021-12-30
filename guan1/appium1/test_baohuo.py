# import threading
#
# from appium1.base import Base
#
#
# class TestBaohuo:
#
#     def setup_class(self):
#         self.b=Base()
#
#     def test_connect_app(self):
#         thread_list=[threading.Thread(target=self.b.connect_devices,args=('emulator-5554',4723,'ue_a')),
#                      threading.Thread(target=self.b.connect_devices,args=('emulator-5556',4725,'ue_b'))]
#         [i.start() for i in thread_list]
#         [i.join() for i in thread_list]
import os

import pytest
from appium import webdriver


class TestBaohuo:
    def test_connect_devices(self, udid, port, client):
        self.udid = udid
        self.port = port
        self.client = client

        desired_caps = {
            'platformName': 'android',
            'udid': udid,
            'deviceName': udid,
            'noReset': True,
        }
        driver = webdriver.Remote('http://127.0.0.1:' + str(port) + '/wd/hub', desired_caps)

        return driver

    def test_launch(self, udid):
        for i in ['com.android.chrome/com.google.android.apps.chrome.Main',
                  'com.android.settings/com.android.settings.Settings']:
            os.system('adb -s ' + udid + ' shell am start -W -n ' + i)

    def test_a(self):

        b = TestBaohuo()
        self.ue_a = b.test_connect_devices('emulator-5554', 4723, 'ue_a')
        self.ue_b = b.test_connect_devices('emulator-5556', 4725, 'ue_b')
        for i in ('emulator-5554', 'emulator-5556'):
            b.test_launch(i)
        self.ue_a.keyevent('3')
        self.ue_b.keyevent('3')
