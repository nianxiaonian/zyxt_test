import time

from utils.param_case import ParametrizedTestCase
from page.home_page import HomePage


class HomeTest(ParametrizedTestCase):
    '''首页相关'''

    @classmethod
    def setUpClass(cls):
        super(HomeTest, cls).setUpClass()
        cls.home_page = HomePage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        super(HomeTest, cls).tearDownClass()

    def test_message(self):
        '''点击公告'''
        self.home_page.click_message_btn()
        time.sleep(2)
        self.driver.keyevent(keycode=4)
        time.sleep(2)

    def test_service(self):
        '''点击客服'''
        self.home_page.click_service_btn()
        time.sleep(2)
        self.driver.keyevent(keycode=4)
        time.sleep(2)

    def test_banner(self):
        '''点击banner轮播图'''
        self.home_page.click_banner()
        time.sleep(2)
        self.driver.keyevent(keycode=4)
        time.sleep(2)

    def test_news(self):
        '''点击中业头条'''
        self.home_page.click_news()
        time.sleep(2)
        self.driver.keyevent(keycode=4)
        time.sleep(2)

    def test_switch_home_product_mine(self):
        '''底部导航 首页-产品-我 切换'''
        self.home_page.click_mine_btn()
        self.home_page.click_product_btn()
        # self.home_page.home_btn()







