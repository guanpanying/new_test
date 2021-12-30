import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.skip
def test_scroll_sele():
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com/')
    driver.maximize_window()
    driver.implicitly_wait(5)

    driver.find_element(By.ID, 'kw').send_keys('朱一龙')
    driver.find_element(By.ID, 'su').click()
    ele = driver.find_element(By.XPATH, '//*[@id="9"]/h3/a')
    driver.execute_script('document.documentElement.scrollTop=1000')
    driver.execute_script('arguments[0].scrollIntoView();', ele)
    print(ele.text)
    time.sleep(3)


@pytest.mark.skip
def test_a():
    a = ["a1", "b2", "c3"]
    b = ':'.join(a)
    print(b)
    print(time.time())


def hi(name='yasoob'):
    return "hi" + name


print(hi())
