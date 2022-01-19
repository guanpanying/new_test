import logging
import time

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException

from app.pageobject2.page.exception import exception_handles

_black_list = [(MobileBy.ID,'tv_agree'),(MobileBy.XPATH,'//*[@text="确定"]')]

class BasePage:
    def __init__(self,driver:WebDriver=None):
        self.driver=driver

    def log_info(self,message):
        logging.info(message)

    @exception_handles
    def find(self,by,value):
        #查找元素
        self.log_info('find element')
        self.log_info(by)

        return self.driver.find_element(by,value)

    def find_and_click(self,by,value):
        #查找元素并点击
        self.find(by,value).click()

    def find_and_input(self,by,value,text):
        #查找元素并输入
        self.find(by,value).send_keys(text)

    def swip_find(self,text,num=3):
        for i in range(num):
            try:

                ele=self.driver.find_element(MobileBy.XPATH,f'//*[@text={text}]')
                return ele
            except:
                print('没有找到，滑一下')
                size=self.driver.get_window_size()
                width=size.get['width']
                height=size.get['height']
                start_x=width/2
                start_y=height*0.8
                end_x=start_x
                end_y=height*0.4
                #滑动时长
                duration =2000

                self.driver.swipe(start_x,start_y,end_x,end_y,duration)
                if i==num-1:
                    raise NoSuchElementException(f'找了{num}次，未找到')

    def get_toast_text(self):
        time.sleep(1)
        text=self.driver.find_element(MobileBy.XPATH,
            '//*[class="android.widget.Toast"]').get_attribute('text')
        return text

