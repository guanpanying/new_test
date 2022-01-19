from app.pageobject2.page.app import App
import pytest
import logging

from app.pageobject2.utils.utils import Utils


class TestAddMember:
    def setup_class(self):
        self.app=App()

    def setup(self):

        self.main=self.app.start().goto_main()

    def teardown(self):
        self.app.stop()


    def test_login(self):
        # name=Utils.get_name()
        import logging
        self.app.log_info('aaaaaaaaa')
        result = self.main.goto_my_tab().click_login().edit_contact().verify_login_toast()
        # assert result=='登录成功'
        assert result == True
        self.app.log_info('b'*10)

    def test_login_fail(self):
        pass
