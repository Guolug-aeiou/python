import time

from appium import webdriver
from appium.options.android import UiAutomator2Options


def main():
    desired_caps = {
        "platformName": "Android",
        "platformVersion": "9",  # 通过 adb 获取
        "deviceName": "MI 6",  # 设备实际型号
        "appPackage": "com.chaoxing.mobile",
        "appActivity": ".main.ui.MainTabActivity",

    }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',
                              options=UiAutomator2Options().load_capabilities(desired_caps))
    time.sleep(2)
    driver.background_app(5)
    time.sleep(2)
    driver.quit()


if "__main__" == __name__:
    main()
