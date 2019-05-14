class Swipe(object):

    def __init__(self, driver):
        self.driver = driver
        self.width = self.get_size()[0]
        self.height = self.get_size()[1]

    def get_size(self):
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        return width, height

    # 向左滑动
    def swipe_left(self):
        x1 = int(self.width * 0.75)
        y1 = int(self.height * 0.5)
        x2 = int(self.width * 0.25)
        self.driver.swipe(x1, y1, x2, y1)

    # 向右滑动
    def swipe_right(self):
        x1 = int(self.width * 0.25)
        y1 = int(self.height * 0.5)
        x2 = int(self.width * 0.75)
        self.driver.swipe(x1, y1, x2, y1)

    # 向上滑动
    def swipe_up(self):
        x1 = int(self.width * 0.5)
        y1 = int(self.height * 0.75)
        y2 = int(self.height * 0.25)
        self.driver.swipe(x1, y1, x1, y2)

    # 向下滑动
    def swipe_down(self):
        x1 = int(self.width * 0.5)
        y1 = int(self.height * 0.25)
        y2 = int(self.height * 0.75)
        self.driver.swipe(x1, y1, x1, y2)





from base.base_driver import BaseDriver
import time
if __name__ == '__main__':
    driver = BaseDriver().driver(0)
    swipe_page = Swipe(driver)
    print(swipe_page.get_size())
    swipe_page.swipe_down()
    time.sleep(2)
    swipe_page.swipe_up()

