from selenium.webdriver.common.by import By
from page.base_page import BasePage
from page.contact_page import ContactPage


class HomePage(BasePage):

    # 重写basepage的base_url
    base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def goto_contact_page(self):
        """
        从导航栏进入通讯录页面
        :return:
        """
        contenter_btn = (By.CSS_SELECTOR, ".frame_nav_item:nth-child(2)")
        self.click_action(contenter_btn)
        return ContactPage()


if __name__ == '__main__':
    HomePage().goto_contact_page().add_department('部门5')