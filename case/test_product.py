import time

from page.product_page import ProductPage
from utils.param_case import ParametrizedTestCase
from utils.swipe import Swipe


class ProductTest(ParametrizedTestCase):
    '''产品相关'''

    @classmethod
    def setUpClass(cls):
        super(ProductTest, cls).setUpClass()
        cls.product_page = ProductPage(cls.driver)
        cls.swipe = Swipe(cls.driver)

    @classmethod
    def tearDownClass(cls):
        super(ProductTest, cls).tearDownClass()

    # def test_service(self):
    #     '''点击客服'''
    #     self.product_page.click_service_btn()
    #     time.sleep(2)
    #     self.driver.keyevent(keycode=4)
    #     time.sleep(2)

    def test_swipe(self):
        '''页面下拉、上滑'''
        self.swipe.swipe_down()
        time.sleep(2)
        self.swipe.swipe_up()
        time.sleep(2)
        self.swipe.swipe_up()
        time.sleep(2)
