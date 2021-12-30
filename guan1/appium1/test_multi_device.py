from appium1.base import Base
from appium import webdriver


class TestMulti:
    b = Base()
    devices = ['emulator-5554', 'emulator-5556']

    def test_kill_process(self):
        pass
