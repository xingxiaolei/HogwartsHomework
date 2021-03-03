import allure
import pytest
import time

t = str(int(time.time()))[-4:]

@allure.feature('我的企业模块')
class TestMyCompany:

    @allure.story('测试修改公司地址')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_edit_company_addr(self, home_ini):
        """
        测试 修改公司名称
        :return:
        """
        company_addr = f"北京市{t}"

        with allure.step('进入我的企业页面'):
            my_company_page = home_ini.goto_my_company()

        with allure.step('修改公司地址操作'):
            my_company_page.edit_company_addr(company_addr)

        with allure.step('获取修改后的公司地址'):
            actual_company_addr = my_company_page.get_company_addr()
            print(actual_company_addr)
            print(company_addr)

        pytest.assume(company_addr == actual_company_addr)
