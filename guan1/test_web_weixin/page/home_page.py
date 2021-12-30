from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_web_weixin.page.add_member_page import AddMemberPage
from test_web_weixin.page.base_page import BasePage
from test_web_weixin.page.contact_page import ContactPage


class HomePage(BasePage):
    def goto_add_member(self):
        '''跳转到添加成员页面'''
        self.driver.find_element(By.XPATH, '//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[1]/div/span[2]').click()
        return AddMemberPage(self.driver)

    def goto_contact(self):
        ele = self.driver.find_element(By.XPATH, '//*[@id="menu_contacts"]/span')
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of(ele))
        self.driver.find_element(By.XPATH, '//*[@id="menu_contacts"]/span').click()
        try:

            self.driver.find_element(By.CSS_SELECTOR,
                                     '#js_contacts50 > div > div.member_colRight > div > div.js_party_info > div.js_has_member > div:nth-child(1) '
                                     '> a.qui_btn.ww_btn.js_add_member')
        except StaleElementReferenceException:
            self.driver.find_element(By.CSS_SELECTOR,
                                     '#js_contacts50 > div > div.member_colRight > div > div.js_party_info > div.js_has_member > div:nth-child(1) '
                                     '> a.qui_btn.ww_btn.js_add_member').click()
        return ContactPage(self.driver)
