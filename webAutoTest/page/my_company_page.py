from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from page.base_page import BasePage


class MyCompanyPage(BasePage):

    def get_company_addr(self):
        """
        获取当前公司地址
        :return:
        """
        company_addr_loc = (By.CSS_SELECTOR, ".profile_enterprise_itemGroup:nth-child(2) .profile_enterprise_item_address")
        company_addr = self.find(company_addr_loc).text
        return company_addr

    def edit_company_addr(self, company_addr):
        """
        修改公司地址
        :return:
        """
        edit_btn = (By.CSS_SELECTOR, ".js_addr_edit_btn")
        addr_input = (By.CSS_SELECTOR, ".inputDlg_item_right .qui_inputText")
        submit_btn = (By.CSS_SELECTOR, ".qui_dialog_foot .ww_btn_Blue")

        back_keys = Keys.BACK_SPACE

        self.click_action(edit_btn)
        # self.double_and_click(addr_input)
        # self.send(addr_input, back_keys)
        self.clear_send(addr_input)
        self.send(locator=addr_input, content=company_addr)
        self.click_action(submit_btn)