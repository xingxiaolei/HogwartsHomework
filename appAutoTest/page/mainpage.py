from appAutoTest.page.basepage import BasePage
from appAutoTest.page.contacrpage import ContactPage
from appAutoTest.page.app import App
from operator import methodcaller
import sys


class MainPage:

    def __init__(self):
        # self.driver = driver
        # self.basepage = BasePage(self.driver)
        self.basepage = App().get_basepage()

        # 获取mainpage的页面数据
        self.data = self.basepage.getData(self.__class__.__name__)

    def goto_contact_page(self):
        """
        进入 通讯录页面
        :return:
        """
        # 获取当前方法的页面数据
        cur_data = self.data[self.basepage.getFunctionName()]
        # methodcaller循环执行页面数据，第一个参数是函数名，第二个参数是元素定位
        for step in cur_data:
            methodcaller(step['action'], step['locator'])(self.basepage)
        return ContactPage(self.basepage)

