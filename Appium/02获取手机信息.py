from appium import webdriver
from appium.options.android import UiAutomator2Options
from a_tools import tools
# 设置终端参数项
# 获取设备 ID
print(tools.run_shell_get_output("adb", "devices"))
# Android 版本
print(tools.run_shell_get_output("adb", "shell getprop ro.build.version.release"))
# 设备型号
print(tools.run_shell_get_output("adb", "shell getprop ro.product.model"))
# 当前前台应用信息
print(tools.run_shell_get_output("adb", "shell dumpsys window | findstr mCurrentFocus"))
# 启动软件并获取启动时间
print(tools.run_shell_get_output("adb", "shell am start -W -n com.chaoxing.mobile/.main.ui.MainTabActivity"))

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
