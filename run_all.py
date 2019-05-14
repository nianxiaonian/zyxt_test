from utils.send_mail import SendMail
from utils.server import Server
import unittest
import HTMLTestRunner
from utils.get_device import GetDevice
import multiprocessing
import time
from case.test_home import HomeTest
from case.test_product import ProductTest
from base.base_driver import BaseDriver
from utils.param_case import ParametrizedTestCase


def get_suite(driver):
    suite = unittest.TestSuite()
    suite.addTest(ParametrizedTestCase.parametrize(HomeTest, param=driver))
    suite.addTest(ParametrizedTestCase.parametrize(ProductTest, param=driver))
    report_path = '/Users/nianzhidan/PycharmProjects/zyxr_new/report/report'+str(i)+'.html'
    with open(report_path, 'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='zyxr测试', verbosity=2)
        runner.run(suite)
    SendMail('nian.zhidan@zyxr.com', 'nian.zhidan@zyxr.com', 'Nzd187', ['nian.zhidan@zyxr.com', '1564043999@qq.com'], report_path).send()


def get_count():
    get_device = GetDevice()
    count = get_device.get_lines()
    print('count:', count)
    return count

if __name__ == '__main__':
    server = Server()
    server.main()
    time.sleep(5)

    processes = []
    for i in range(get_count()):
        print('i: ', i)
        driver = BaseDriver().android_driver(i)
        t = multiprocessing.Process(target=get_suite, args=(driver,))
        processes.append(t)
    # 为了多个设备可以同时执行用例
    for j in processes:
        j.start()
        j.join()
        server.kill_server(processes.index(j))

    time.sleep(10)




