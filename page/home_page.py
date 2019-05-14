from selenium.webdriver.common.by import By

from .base_page import BasePage


class HomePage(BasePage):

    # 首页按钮
    home_btn = (By.ID, 'com.zyxr.home.toulfhome:id/m_')
    def click_home_btn(self):
        self.find_element(*self.home_btn).click()

    # 产品按钮
    product_btn = (By.ID, 'com.zyxr.home.toulfhome:id/ma')
    def click_product_btn(self):
        self.find_element(*self.product_btn).click()

    # 我按钮
    mine_btn = (By.ID, 'com.zyxr.home.toulfhome:id/mc')
    def click_mine_btn(self):
        self.find_element(*self.mine_btn).click()

    # 消息按钮
    message_btn = (By.ID, 'com.zyxr.home.toulfhome:id/a17')
    def click_message_btn(self):
        self.find_element(*self.message_btn).click()

    # 客服按钮
    service_btn = (By.ID, 'com.zyxr.home.toulfhome:id/a2n')
    def click_service_btn(self):
        self.find_element(*self.service_btn).click()

    # banner轮播图
    banner = (By.ID, 'com.zyxr.home.toulfhome:id/h')
    def click_banner(self):
        self.find_element(*self.banner).click()

    # 中业头条
    news = (By.ID, 'com.zyxr.home.toulfhome:id/a2q')
    def click_news(self):
        self.find_element(*self.news).click()

