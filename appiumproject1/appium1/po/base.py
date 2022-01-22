from appium import webdriver

class Base:
    def __init__(self,udid,port):
        caps={}
        caps['udid']=udid
        caps['deviceName']=udid
        caps['platform']='android'
        caps['noReset']='true'
        caps['appPackage']='com.android.settings'
        caps['appActivity']='com.android.settings.homepage.SettingsHomepageActivity'

        driver=webdriver.Remote('http://127.0.0.1:'+str(port)+'/wd/hub',caps)




