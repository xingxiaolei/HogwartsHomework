from UIAutoTestFrame.page.base_page import BasePage
from UIAutoTestFrame.page.contact_page import ContactPage


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.name = self.__class__.__name__

    def goto_contact(self):
        self.steps(self.name)
        return ContactPage(self._driver)


