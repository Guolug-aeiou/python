import time

from appium import webdriver
from appium.options.android import UiAutomator2Options

def main():
    desired_caps = {
        "platformName": "Android",
        "platformVersion": "9",  # 通过 adb 获取
        "deviceName": "MI 6",  # 设备实际型号
        "appPackage": "com.taobao.taobao",
        "appActivity": "com.taobao.tao.welcome.Welcome"
    }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',
                              options=UiAutomator2Options().load_capabilities(desired_caps))
    time.sleep(1)
    driver.close_app()
    # 关闭驱动
    time.sleep(5)
    driver.quit()

if "__main__" == __name__:
    main()
