from operator import methodcaller
import inspect

class ContactPage:
    def __init__(self, basepage):
        # self.driver = driver
        self.basepage =basepage

        # 获取mainpage的页面数据
        self.data = self.basepage.getData(self.__class__.__name__)

    def add_member(self, name, phone):
        """
        通讯录添加成员
        :return:
        """
        # 获取当前方法的页面数据(带有变量的模板)
        data = self.data[self.basepage.getFunctionName()]
        values = {'name': name, 'phone': phone}

        # 进行变量替换
        cur_data = self.basepage.get_template_data(data, values)

        # methodcaller循环执行页面数据
        for step in cur_data:
            if len(step.keys()) ==3:
                methodcaller(step['action'], step['locator'], step['content'])(self.basepage)
            elif len(step.keys()) ==2:
                methodcaller(step['action'], step['locator'])(self.basepage)

    def go_back(self):
        # 模拟点击手机的返回键
        self.basepage.driver.press_keycode(4)

    def find_member(self, name):
        """
        查找通讯录成员
        :param name:
        :return:
        """
        # 获取当前方法的页面数据(带有变量的模板)
        data = self.data[self.basepage.getFunctionName()]

        values = {'name': name}

        # 进行变量替换
        cur_data = self.basepage.get_template_data(data, values)
        # methodcaller循环执行页面数据
        for step in cur_data:
            if len(step.keys()) == 3:
                methodcaller(step['action'], step['locator'], step['content'])(self.basepage)
            elif len(step.keys()) == 2:
                methodcaller(step['action'], step['locator'])(self.basepage)
