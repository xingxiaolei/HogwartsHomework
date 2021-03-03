from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    base_url = ""

    def __init__(self, driver: WebDriver = None):
        if driver is None:
            option = Options()
            #复用浏览器
            option.debugger_address = '127.0.0.1:9999'
            self.driver = webdriver.Chrome(options=option)
        else:
            self.driver = driver
        self.driver.implicitly_wait(5)

        if self.base_url != "":
            self.driver.get(self.base_url)

    def find(self, locator):
        '''
        查找元素，直到元素可见
        :param locator: 元组
        :return:
        '''
        ele = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(locator))
        # ele = WebDriverWait(self.driver, 5).until(lambda x:x.find_element(*locator))
        return ele

    def finds(self, locator):
        '''
        查找多个元素，返回元素对象列表
        :param locator: 元组
        :return:
        '''
        eles = self.driver.find_elements(*locator)
        return eles

    def click_action(self, locator):
        """
        点击操作
        :param locator: 元组
        :return:
        """
        ele = self.find(locator)
        ele.click()

    def send(self, locator, content):
        '''
        输入框输入内容
        :param locator: 元组
        :param content: 输入的内容，字符串
        :return:
        '''
        ele = self.find(locator)
        ele.send_keys(content)


    def clear_send(self, locator):
        """
        清空输入框
        :param locator:
        :return:
        """
        ele = self.find(locator)
        ele.clear()

    def double_and_click(self, locator):
        """
        双击元素
        :param locator:
        :return:
        """
        ele = self.find(locator)
        ActionChains(self.driver).double_click(ele).perform()

    def get_screen_shot(self):
        """
        获取截图
        :return:
        """
        pass


