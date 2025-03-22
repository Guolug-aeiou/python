import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions.interaction import POINTER_TOUCH

from a_tools.tools import get_element_centre


def main():
    desired_caps = dict(
        platformName="Android",  # 固定为 "Android" 或 "iOS"，不可随意命名
        platformVersion="9",  # 通过 `adb shell getprop ro.build.version.release` 获取
        deviceName="MI 6",  # 设备型号，仅用于日志展示，不影响实际连接
        noReset=True,  # 不重置应用状态（保留登录信息、缓存等）
        udid="2aa7ef23",  # 通过 `adb devices` 获取
        automationName="UiAutomator2",  # Android 的默认驱动，必须明确指定
        newCommandTimeout=300,  # 300 秒内无新命令则自动关闭会话
    )
    # 初始化驱动
    driver = webdriver.Remote(
        'http://localhost:4723',
        options=UiAutomator2Options().load_capabilities(desired_caps))
    # 获取屏幕分辨率
    print(driver.get_window_size())
    # 获取截图
    time_now = time.strftime('%Y_%m_%d %H_%M_%S')
    driver.get_screenshot_as_file(f'./image/{time_now}.png')
    # 获取当前网络情况
    print(driver.network_connection)
    """    Possible values:
    +--------------------+------+------+---------------+
    | Value (Alias)      | Data | Wifi | Airplane Mode |
    +====================+======+======+===============+
    | 0 (None)           | 0    | 0    | 0             |
    +--------------------+------+------+---------------+
    | 1 (Airplane Mode)  | 0    | 0    | 1             |
    +--------------------+------+------+---------------+
    | 2 (Wifi only)      | 0    | 1    | 0             |
    +--------------------+------+------+---------------+
    | 4 (Data only)      | 1    | 0    | 0             |
    +--------------------+------+------+---------------+
    | 6 (All network on) | 1    | 1    | 0             |
    +--------------------+------+------+---------------+ """
    # 设置网络
    # driver.set_network_connection(4)
    # 向手机按下音量减、
    driver.press_keycode(25)
    driver.press_keycode(25)
    # 向手机按下 home 按键
    driver.press_keycode(3)
    # 打开手机通知栏
    driver.open_notifications()
    driver.quit()


if "__main__" == __name__:
    main()
