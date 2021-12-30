from selenium.webdriver.common.by import By

from test_web_weixin.page.base_page import BasePage


class ContactPage(BasePage):
    _member_list = (By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')

    def add_member(self):
        """
        添加成员操作
        :return:
        """
        pass

    def get_member(self):
        """获取成员列表，用来做断言"""
        member_list = self.finds(*self._member_list)
        member_list2 = [i.text for i in member_list]

        # for i in member_list:
        #     member_list2.append(i.text)
        return member_list2
