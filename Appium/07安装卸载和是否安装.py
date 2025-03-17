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
    driver.remove_app("com.microsoft.emmx")
    time.sleep(5)
    driver.install_app(r"D:\下载缓存点\华测\Appium env\apk\edge.apk")
    time.sleep(5)
    print("是否安装了应用" + driver.is_app_installed("com.microsoft.emmx") if "是" else "否")
    driver.quit()

if "__main__" == __name__:
    main()
