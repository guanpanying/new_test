from test_appium.po.page.base import Base
from test_appium.po.page.contact import Contact


class Main(Base):
    '''app首页'''

    def goto_contact(self):
        # 点击通讯录按钮

        return Contact(self.driver)
