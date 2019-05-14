from appium import webdriver
import time
from utils.get_device import GetDevice


class BaseDriver(object):

    def __init__(self):
        self.opera_device = GetDevice()

    def android_driver(self, i):
        port = self.opera_device.get_value('device_info_%s' % i, 'port')
        device_name = self.opera_device.get_value('device_info_%s' % i, 'deviceName')
        capabilities = {
			"platformName": "Android",
			"automationName": "UiAutomator2",
			"deviceName": device_name,
			"app": "/Users/nianzhidan/PycharmProjects/zyxr_new/app/app_test_5.0.0.apk",
			"appWaitActivity": "com.zyxr.home.toulfhome.activity.MainActivity",
			"noReset": "true",
		}
        driver = webdriver.Remote("http://127.0.0.1:" + str(port) + "/wd/hub", capabilities)
        time.sleep(10)
        return driver

if __name__ == '__main__':
    driver = BaseDriver()
    driver = driver.android_driver(0)
    driver.quit()

