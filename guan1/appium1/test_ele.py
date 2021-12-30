# -*-coding:utf-8-*-
from selenium import webdriver
import time as t

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.baidu.com')
driver.find_element_by_id('u1').find_element_by_class_name('lb').click()
t.sleep(3)
driver.find_element_by_id('TANGRAM__PSP_10__footerULoginBtn').click()
t.sleep(3)
print(driver.find_element_by_id('TANGRAM__PSP_10__memberPass').is_selected())
driver.quit()
