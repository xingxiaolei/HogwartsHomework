from UIAutoTestFrame.app.app import App
from UIAutoTestFrame.page.contact_page import ContactPage
import time

t = str(int(time.time()))[-4:]


class TestContact:
    name = f'aaa_{t}'
    account = f'aaa_{t}'
    phone = f'1300000{t}'

    def setup_class(self):
        self.app = App()
        self.main_page = self.app.start().main()

    def setup(self):
        self.contact_page = self.main_page.goto_contact()

    def teardown_class(self):
        self.app.stop()

    def test_add_member(self):

        self.contact_page.add_member(self.name, self.phone)
        self.contact_page.back()
        self.contact_page.find_member(self.name)
        self.contact_page.back()


    def test_del_member(self):
        self.contact_page.del_member(self.name)


