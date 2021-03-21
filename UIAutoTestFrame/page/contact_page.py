from UIAutoTestFrame.page.base_page import BasePage


class ContactPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.name = self.__class__.__name__

    def add_member(self, name, phone):
        self._params['name'] = name
        self._params['phone'] = phone

        self.steps(self.name)

    def find_member(self, name):
        self._params['name'] = name

        self.steps(self.name)

    def del_member(self, name):
        self._params['name'] = name

        self.steps(self.name)


