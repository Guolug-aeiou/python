
from appium import webdriver
from appium.options.android import UiAutomator2Options

# 设置终端参数项
# 发送指令给到 appium server
desired_caps = {
    "platformName": "Android",
    "platformVersion": "9",  # 通过 adb 获取
    "deviceName": "MI 6",  # 设备实际型号
    "udid": "2aa7ef23",  # adb devices 获取的设备ID
    "appPackage": "com.chaoxing.mobile",
    "appActivity": ".main.ui.MainTabActivity",
    "noReset": False,  # 真机建议关闭 noReset
    "automationName": "UiAutomator2",
}
# appium server 进行启动
# 发送指令给到 appium server
webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=UiAutomator2Options().load_capabilities(desired_caps))
# appium server 处于启动状态
# 模拟器或真机被电脑识别
# 进行连接再查看连接设备 如何
