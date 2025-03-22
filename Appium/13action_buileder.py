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
    # 创建 ActionBuilder 对象
    actions = ActionBuilder(driver)
    # 创建 PointerInput 对象
    pointer = PointerInput(POINTER_TOUCH, "touch")
    # 将 PointerInput 添加到 ActionBuilder
    actions.add_pointer_input(pointer.kind, pointer.name)
    # 使用 pointer_action 定义操作
    actions.pointer_action.move_to_location(
        x=get_element_centre(driver.find_element(by=AppiumBy.XPATH, value='//*[@content-desc="抖音"]'))[0],
        y=get_element_centre(driver.find_element(by=AppiumBy.XPATH, value='//*[@content-desc="抖音"]'))[1]
    ).click()
    # 执行操作
    actions.perform()
    actions.pointer_action.move_to_location(
        x=get_element_centre(driver.find_element(by=AppiumBy.XPATH,value='//android.widget.TextView[contains(@content-desc,"关注")]'))[0],
        y=get_element_centre(driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[contains(@content-desc,"关注")]'))[1]
    ).click()
    actions.perform()
    driver.quit()


if "__main__" == __name__:
    main()
