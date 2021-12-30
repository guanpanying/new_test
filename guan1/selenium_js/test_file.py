from time import sleep

from selenium_js.base import Base1


class TestFile(Base1):
    def test_file(self):
        self.driver.get('https://www.baidu.com')
        self.driver.find_element_by_xpath('//*[@id="form"]/span[1]/span[2]').click()
        self.driver.find_element_by_css_selector('upload-pic').send_keys(
            '/Users/guanpy/Desktop/guan1/selenium_js/baidu.png')

        sleep(3)
