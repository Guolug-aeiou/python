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
    time.sleep(5)
    # 跳转到其他应用
    try:
        driver.start_activity("com.chaoxing.mobile", "com.chaoxing.mobile.activity.SplashActivity")
        print("Activity started successfully.")
    except Exception as e:
        print(f"Failed to start activity: {e}")

    # 关闭驱动
    time.sleep(5)
    driver.quit()

if "__main__" == __name__:
    main()
