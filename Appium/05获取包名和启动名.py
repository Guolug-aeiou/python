import time

from appium import webdriver
from appium.options.android import UiAutomator2Options


def main():
    desired_caps = {
        "platformName": "Android",
        "platformVersion": "9",  # 通过 adb 获取
        "deviceName": "MI 6",  # 设备实际型号
    }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',
                              options=UiAutomator2Options().load_capabilities(desired_caps))
    # 跳转到其他应用
    while True:
        print("包名：" + driver.current_package)
        print("启动名：" + driver.current_activity)
        time.sleep(5)
    # 关闭驱动
    driver.quit()


if "__main__" == __name__:
    main()
