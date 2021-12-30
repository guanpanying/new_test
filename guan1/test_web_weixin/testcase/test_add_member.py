from test_web_weixin.page.base_page import BasePage
from test_web_weixin.page.home_page import HomePage


class TestAddMember:
    def setup_class(self):
        self.home = HomePage()

    def test_add_member(self):
        """
        添加成员测试用例
        :return:
        """
        # 1。跳转添加成员页面 2。添加成员 3、自动跳转到通讯录页面
        res = self.home.goto_add_member().add_member().get_member()
        assert 'guan盼' in res

    def test_add_member_by_contact(self):
        """
        通过通讯录页面添加成员
        :return:
        """
        self.home.goto_contact().add_member()

    def teardown_class(self):
        self.home.quit()
