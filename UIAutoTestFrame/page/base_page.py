# -*- coding:utf-8 -*-
import inspect
import json

import yaml
import os

from UIAutoTestFrame.utils.log import log
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from UIAutoTestFrame.utils.wrapper import handle_black

page_data_path = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), "pagedata"))

class BasePage:

    # yaml文件中变量对应的键值对
    _params = dict()

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def set_implicitly(self, time):
        self._driver.implicitly_wait(time)

    def screenshot(self, name):
        self._driver.save_screenshot(name)

    @handle_black
    def finds(self, locator, value: str = None):

        elements: list
        if isinstance(locator, list):
            elements = self._driver.find_elements(*locator)
        else:
            elements = self._driver.find_elements(locator, value)
        return elements

    @handle_black
    def find(self, locator, value: str = None):
        element: WebElement
        if isinstance(locator, list):
            element = self._driver.find_element(*locator)
        else:
            element = self._driver.find_element(locator, value)
        return element

    @handle_black
    def find_and_get_text(self, locator, value: str = None):

        if isinstance(locator, list):
            element_text = self._driver.find_element(*locator).text
        else:
            element_text = self._driver.find_element(locator, value).text
        return element_text

    def get_screenshot(self, filename):
        self._driver.get_screenshot_as_file(filename)

    @handle_black
    def scroll_find(self, text):
        """
        滑动查找 带有text属性的元素
        :param text:
        :return:
        """
        element = self._driver.find_element_by_android_uiautomator(
            f'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("{text}").instance(0));'
        )
        return element

    def get_yaml_path(self, name):
        """
        获取yaml文件路径
        :param name:
        :return:
        """
        path = os.path.abspath(os.path.join(page_data_path, name+".yaml"))
        return path

    def steps(self, cls_name):
        path = self.get_yaml_path(cls_name)
        log(f'在{cls_name}页面')
        fun_name = inspect.stack()[1].function
        log(f'准备进行{fun_name}操作')
        with open(path, encoding='utf-8') as f:
            json_data = yaml.safe_load(f)[fun_name]
        str_data = json.dumps(json_data)
        log(f'获取到{fun_name}操作的元素数据：{json_data}')

        # 替换yaml文件中变量，匹配所有找到的变量，如果未匹配到原样返回
        for key, value in self._params.items():
            str_data = str_data.replace('${' + key + '}', value)
        json_data = json.loads(str_data)
        log(f'{fun_name}操作变量替换后的数据：{json_data}')

        for step in json_data:
            if "action" in step.keys():
                action = step['action']
                if "find" == action:
                    log(f'对{step["locator"]}进行查找操作。')
                    self.find(step['locator'])

                if "find_click" == action:
                    log(f'对{step["locator"]}进行点击操作。')
                    self.find(step['locator']).click()

                if "send" == action:
                    log(f'对{step["locator"]}输入值{step["value"]}。')
                    self.find(step['locator']).send_keys(step['value'])

                if "scroll_find" == action:
                    log(f'对{step["locator"]}进行滑动查找操作')
                    self.scroll_find(step['locator']).click()


    def back(self):
        self._driver.back()

















































    