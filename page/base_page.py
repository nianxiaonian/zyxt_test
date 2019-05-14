from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    # 从写元素定位的方法，使用显式等待，查找元素
    def find_element(self, *args):
        try:
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(args))
            return self.driver.find_element(*args)
        except:
            print('页面未找到%s元素' % args)

    def find_elements(self, *args):
        try:
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(args))
            return self.driver.find_elements(*args)
        except Exception as e:
            print(e)
            print('页面未找到%s元素' % args)

    # 封装长按元素方法
    def long_press(self, args, t):
        TouchAction(self.driver).long_press(args, duration=t).perform()

    # 重写send_keys方法
    def send_keys(self, args, value, clear_first=True, click_first=True):
        try:
            if click_first:
                self.find_element(*args).click()
            if clear_first:
                self.find_element(*args).clear()
                self.find_element(*args).send_keys(value)
        except Exception as e:
            print(e)
            print('页面未找到%s元素' % args)

    # 封装判断是否存在toast消息，存在返回True,不存在返回False
    def is_toast_exist(self, text):
        try:
            toast_loc = (By.XPATH, "//*[contains(@text,'%s')]" % text)
            # 显示等待 WebDriverWait()
            WebDriverWait(self.driver, 20, 0.01).until(EC.presence_of_element_located(toast_loc))
            return True
        except Exception as e:
            print(e)
            return False







