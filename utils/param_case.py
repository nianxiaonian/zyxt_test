import unittest


class ParametrizedTestCase(unittest.TestCase):
    def __init__(self, methodName='runTest', param=None):
        super(ParametrizedTestCase, self).__init__(methodName)
        global params
        params = param

    @classmethod
    def setUpClass(cls):
        cls.driver = params

    @classmethod
    def tearDownClass(cls):
        cls.driver.close_app()
        cls.driver.quit()


    def parametrize(testcase_class, param=None):
        print('parametrize--param: ', param)
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_class)
        suite = unittest.TestSuite()
        for name in testnames:
            suite.addTest(testcase_class(name, param=param))
        return suite



