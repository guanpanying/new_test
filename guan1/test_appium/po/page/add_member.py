from test_appium.po.page.add_member_info import AddMemberInfo
from test_appium.po.page.base import Base


class AddMember(Base):
    '''添加成员页'''

    def goto_add_member_info(self):
        # 进入添加成员信息页

        return AddMemberInfo(self.driver)
