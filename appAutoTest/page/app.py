from appium import webdriver

from appAutoTest.page.basepage import BasePage
# from appAutoTest.page.mainpage import MainPage


class App:

    def __init__(self):
        self.driver = None
        self.start_app()

    def start_app(self):

        caps = dict()
        caps['platformName'] = "Android"
        caps['deviceName'] = "oppo"
        caps['appPackage'] = "com.tencent.wework"
        caps['appActivity'] = ".launch.LaunchSplashActivity"
        caps['noReset'] = "true"
        caps['autoGrantPermissions'] = 'true'
        caps['unicodeKeyBoard'] = 'true'

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)
        # return self.driver

    # def goto_main_page(self):
    #     """
    #     启动app 进入默认消息页面
    #     :return:
    #     """
    #     return MainPage()

    def get_basepage(self):
        return BasePage(self.driver)


