from selenium.webdriver.common.by import By
from page.base_page import BasePage
from page.contact_page import ContactPage
from page.my_company_page import MyCompanyPage


class HomePage(BasePage):

    # 重写basepage的base_url
    base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def goto_contact_page(self):
        """
        从导航栏进入通讯录页面
        :return:
        """
        contact_btn = (By.CSS_SELECTOR, ".frame_nav_item:nth-child(2)")
        self.click_action(contact_btn)
        return ContactPage()

    def goto_my_company(self):
        """
        从导航栏进入 我的企业
        :return:
        """
        company_btn = (By.CSS_SELECTOR, ".frame_nav_item:nth-child(6)")
        self.click_action(company_btn)
        return MyCompanyPage()



if __name__ == '__main__':
    HomePage().goto_contact_page().add_department('部门5')