from selenium.webdriver.common.by import By

from .base_page import BasePage


class ProductPage(BasePage):

    # 客服按钮
    service_btn = (By.XPATH, '//*[@text="专属顾问"]')
    def click_service_btn(self):
        self.find_element(*self.service_btn).click()

    


