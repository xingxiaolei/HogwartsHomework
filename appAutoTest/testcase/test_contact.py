from appAutoTest.page.mainpage import MainPage
import time

t = str(int(time.time()))[-4:]


class TestContect:

    name = f'aaa_{t}'
    account = f'aaa_{t}'
    phone = f'1300000{t}'

    def test_add_contact(self):
        # 进入通讯录页面
        contact_page = MainPage().goto_contact_page()
        # 添加成员操作
        contact_page.add_member(self.name, self.phone)
        # 返回上一页
        contact_page.go_back()
        # 列表中查找该成员
        contact_page.find_member(self.name)
