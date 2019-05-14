from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time
from utils.sys_cmd import SysCmd


def start_server():

    sys_cmd = SysCmd()
    sys_cmd.excute_cmd('appium -p 4723 -U  1f481550 --no-reset --session-override')
    print('hello')

def get_driver():
    capabilities = {
        "platformName": "Android",
        # "automationName": "UiAutomator2",
        "deviceName": '1f481550',
        "app": "/Users/nianzhidan/PycharmProjects/zyxr_new/app/app_test_4.3.9.apk",
        "appWaitActivity": "com.zyxr.home.toulfhome.activity.MainActivity",
        "noReset": "true",
    }
    print('world')
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities)
    time.sleep(10)
    return driver

if __name__ == '__main__':
    print('eeeeeeee')
    start_server()
    print(1)
    driver = get_driver()
    bottom_btn = driver.find_elements_by_xpath('//*[@class="android.widget.RadioButton"]')
    print(bottom_btn)
    bottom_btn[1].click()
    time.sleep(1)
    bottom_btn[2].click()
    time.sleep(1)
    bottom_btn[0].click()
    time.sleep(1)




