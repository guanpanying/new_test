from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from selenium1.base import Base1


class TestFrame(Base1):
    def test_frame(self):

        self.driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
        try:
            self.driver.switch_to.alert().accept()
        except BaseException:
            print(BaseException)
        self.driver.switch_to.frame('iframeResult')
        sour_ele = self.driver.find_element(By.ID, 'draggable')
        target_ele = self.driver.find_element_by_id('droppable')
        action = ActionChains(self.driver)
        action.drag_and_drop(sour_ele, target_ele)
        action.perform()

        # self.driver.switch_to.default_content()
        # self.driver.find_element_by_id('submitBTN').click()
        sleep(5)
