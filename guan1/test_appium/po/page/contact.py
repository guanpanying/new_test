from test_appium.po.page.add_member import AddMember
from test_appium.po.page.base import Base


class Contact(Base):
    '''通讯录页面'''

    def goto_add_member(self):
        # 点击添加成员

        return AddMember(self.driver)
