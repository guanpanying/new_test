from app.pageobject1.page.app import App
import pytest


class TestAddMember:
    def setup(self):
        self.app=App()
        self.main=self.app.start().goto_main()

    def teardown(self):
        self.app.stop()


    def test_login(self):
        result = self.main.goto_my_tab().click_login().edit_contact().verify_login_toast()
        # assert result=='登录成功'
        assert result == True

    def test_login_fail(self):
        pass
