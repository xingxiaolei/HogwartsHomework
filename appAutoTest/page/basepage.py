import yaml
import os
import inspect
from string import Template

from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

basePath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
dataPath = os.path.join(basePath, 'page_data')


class BasePage(object):

    def __init__(self, driver: WebDriver):

        self.driver = driver

    def getData(self, cls_name) -> dict:
        """
        各个page类，通过自己的类名获取页面数据及行为
        :param cls_name:
        :return:
        """
        data_path = os.path.join(dataPath, cls_name + '.yaml')
        pagedata = yaml.safe_load(open(data_path, 'r', encoding='utf8'))
        return pagedata

    def getFunctionName(self):
        """
        各个page对象的行为方法，通过该函数获取自己的方法名
        :return:
        """
        return inspect.stack()[1][3]

    def get_template_data(self, template, values):
        """
        yaml文件模板替换，
        :param args:
        :return:
        """
        t = Template(str(template))
        ret = t.safe_substitute(values)
        return eval(ret)

    def find(self, locator) -> WebElement:
        ele = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator))
        # ele = self.driver.find_element(*locator)
        return ele

    def find_click(self, locator):
        ele = self.find(locator)
        ele.click()

    def send(self, locator, content):
        ele = self.find(locator)
        ele.send_keys(content)

    def scroll_find(self, text):
        """
        滑动查找 带有text属性的元素
        :param text:
        :return:
        """
        self.driver.find_element_by_android_uiautomator(
            f'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("{text}").instance(0));'
        ).click()




