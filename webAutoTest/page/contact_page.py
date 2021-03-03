
from page.base_page import BasePage
from selenium.webdriver.common.by import By


class ContactPage(BasePage):

    add_member_btn = (By.CSS_SELECTOR, '.js_operationBar_footer .js_add_member')
    member_name = (By.CSS_SELECTOR, "#username")
    member_account = (By.CSS_SELECTOR, "#memberAdd_acctid")
    member_phone = (By.CSS_SELECTOR, "#memberAdd_phone")
    save_btn = (By.CSS_SELECTOR, ".js_btn_save")

    def get_member_name(self):
        """
        获取成员姓名--》列表
        :return:
        """
        name_btn = (By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        eles = self.finds(name_btn)
        names = []
        for ele in eles:
            name = ele.get_attribute('title')
            names.append(name)
        return names

    def get_toast(self):
        """
        添加成员成功，获取toast
        :return:
        """
        toast = (By.CSS_SELECTOR, "#js_tips")
        ele = self.find(toast)
        return ele

    def add_member(self, name, account, phone):
        """
        添加成员
        :param name:
        :param account:
        :param phone:
        :return:
        """
        self.click_action(self.add_member_btn)
        self.send(locator=self.member_name, content=name)
        self.send(locator=self.member_account, content=account)
        self.send(locator=self.member_phone, content=phone)
        self.click_action(self.save_btn)

    def add_department(self, content):
        """
        添加部门,点击 +
        :return:
        """
        add_btn = (By.CSS_SELECTOR, ".js_create_dropdown")
        add_dep_btn = (By.CSS_SELECTOR, ".js_create_party")
        dep_name = (By.CSS_SELECTOR, ".inputDlg_item:nth-child(1) input")
        select_input = (By.CSS_SELECTOR, ".js_toggle_party_list")
        belong_dep = (By.CSS_SELECTOR, ".form .jstree-container-ul>li>a")
        submit_btn = (By.CSS_SELECTOR, "#__dialog__MNDialog__ div .ww_dialog_foot .ww_btn_Blue")

        self.click_action(add_btn)
        self.click_action(add_dep_btn)
        self.send(locator=dep_name, content=content)
        self.click_action(select_input)
        self.click_action(belong_dep)
        self.click_action(submit_btn)

    def search_dep(self, content):
        """
        搜索结果查询，返回查询到的 部门名称列表
        :param content:
        :return:
        """
        search_input = (By.CSS_SELECTOR, "#memberSearchInput")
        search_res = (By.CSS_SELECTOR, "#search_party_list li")

        self.send(locator=search_input, content=content)
        eles = self.finds(search_res)
        names = []
        for ele in eles:
            name = ele.get_attribute('title')
            names.append(name)
        return names



if __name__ == '__main__':
    import time
    t = time.time()
    print(int(t))
    print(str(int(t))[-4:])