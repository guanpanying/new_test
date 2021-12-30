import os

from appium import webdriver
import time
import threading

from appium.webdriver.common.mobileby import MobileBy

desired_caps = {
    'platformName': 'Android',
    'deviceName': '5554',
    'udid': 'emulator-5554',
    'platformVersion': '11',
    'appPackage': 'com.android.chrome',
    'appActivity': 'com.google.android.apps.chrome.Main',
    'noReset': True

}

desired_caps2 = {
    'platformName': 'Android',
    'deviceName': '5556',
    'udid': 'emulator-5556',
    'platformVersion': '10',
    'appPackage': 'com.android.chrome',
    'appActivity': 'com.google.android.apps.chrome.Main',

    'noReset': True
}


def task1():
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    ##休眠20s等待页面加载完成
    driver.implicitly_wait(5)
    driver.get('https://www.baidu.com')
    # os.popen('adb shell ps -A | grep com.android.chrome')
    time.sleep(10)
    driver.quit()


def task2():
    driver = webdriver.Remote('http://127.0.0.1:4725/wd/hub', desired_caps2)
    ##休眠20s等待页面加载完成
    driver.implicitly_wait(5)
    driver.get('https://www.baidu.com')
    time.sleep(10)
    driver.find_element(MobileBy.IMAGE)
    driver.quit()


threads = []
t1 = threading.Thread(target=task1)
threads.append(t1)

t2 = threading.Thread(target=task2)
threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        t.start()
