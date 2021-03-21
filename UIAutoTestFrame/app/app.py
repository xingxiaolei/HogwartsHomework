from appium import webdriver
from UIAutoTestFrame.page.base_page import BasePage
from UIAutoTestFrame.page.main_page import MainPage


class App(BasePage):
    def start(self):
        if self._driver is None:
            caps = dict()
            caps["platformName"] = "Android"
            caps["deviceName"] = "192.168.56.103:5555"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.LaunchSplashActivity"
            caps['noReset'] = "true"
            caps['autoGrantPermissions'] = 'true'
            caps['unicodeKeyBoard'] = 'true'
            # caps['skipServerInstallation'] = True
            # caps['skipDeviceInitialization'] = True
            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

        else:
            self._driver.launch_app()
        self._driver.implicitly_wait(10)
        return self

    def restart(self):
        self._driver.close()
        self._driver.launch_app()

    def stop(self):
        self._driver.terminate_app("com.tencent.wework")

    def main(self):
        return MainPage(self._driver)