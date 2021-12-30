from test_appium.po.page.app import App
from test_appium.po.page.main import Main


class TestAddMember:
    def test_add_member(self):
        aa = App()
        aa.start()
        aa.goto_main().goto_contact().goto_add_member().goto_add_member_info().new_member_info()
