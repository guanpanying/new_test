from selenium.webdriver.common.by import By

from test_web_weixin.page.base_page import BasePage
from test_web_weixin.page.contact_page import ContactPage


class AddMemberPage(BasePage):
    _ele_username = (By.ID, 'username')
    _ele_memberadd_acctid = (By.ID, 'memberAdd_acctid')
    _ele_memberadd_phone = (By.ID, 'memberAdd_phone')
    _ele_save_button = (By.XPATH, '//*[@data-name="contacts"]/div/div[2]/div/div[4]/div/form/div[1]/a[2]')

    def add_member(self):
        self.find(*self._ele_username).send_keys('guan盼')
        self.find(*self._ele_memberadd_acctid).send_keys('001')
        self.find(*self._ele_memberadd_phone).send_keys('18102271778')
        self.find(*self._ele_save_button).click()

        return ContactPage(self.driver)
