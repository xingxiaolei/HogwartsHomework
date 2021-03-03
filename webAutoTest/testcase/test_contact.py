import pytest
import allure
import time

t = str(int(time.time()))[-4:]


@allure.feature('通讯录模块')
class TestContact:

    @allure.story('测试添加成员功能')
    def test_add_member(self, home_ini):
        """
        测试添加成员
        :param home_ini: conftest,初始化home页
        :return:
        """
        name = f'aaa_{t}'
        account = f'aaa_{t}'
        phone = f'1300000{t}'

        with allure.step('进入通讯录页面'):
            contact_page = home_ini.goto_contact_page()

        with allure.step('添加成员操作'):
            contact_page.add_member(name=name, account=account, phone=phone)

        with allure.step('获取toast'):
            toast = contact_page.get_toast()

        # with allure.step('获取成员列表'):
        #     names = contact_page.get_member_name()

        pytest.assume('保存成功' == toast.text)
        # pytest.assume(name in names)


    @allure.story('测试添加部门功能')
    def test_add_dep(self, home_ini):
        """
        测试添加部门
        :param home_ini: conftest,初始化home页
        :return:
        """
        dep_name = f'部门{t}'

        with allure.step('进入通讯录页面'):
            contact_page = home_ini.goto_contact_page()

        with allure.step('添加部门操作'):
            contact_page.add_department(dep_name)

        with allure.step('获取搜索结果'):
            search_res = contact_page.search_dep(dep_name)

        ret = ''
        for i in search_res:
            if dep_name in i:
                ret = i

        pytest.assume(dep_name in ret)



