from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class TestList:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_l(self):
        self.driver.get('https://www.runoob.com/try/try.php?filename=trycss_dropdown_text')
        self.driver.switch_to.frame('iframeResult')
        action = ActionChains(self.driver)

        action.move_to_element(self.driver.find_element(By.XPATH, '//*[@class="dropdown"]/span')).pause(5).perform()
        print(self.driver.find_element(By.XPATH, '//*[@class="dropdown-content"]/p[1]').text)
