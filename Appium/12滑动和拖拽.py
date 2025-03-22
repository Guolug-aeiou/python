
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy


def main():
    desired_caps = dict(
        # 平台类型（必须正确）
        platformName="Android",  # 固定为 "Android" 或 "iOS"，不可随意命名
        # 设备系统版本（需与实际一致）
        platformVersion="9",  # 通过 `adb shell getprop ro.build.version.release` 获取
        # 设备名称（展示用，可自定义）
        deviceName="MI 6",  # 设备型号，仅用于日志展示，不影响实际连接
        # 会话复用配置
        noReset=True,  # 不重置应用状态（保留登录信息、缓存等）
        # 设备唯一标识（关键配置！）
        udid="2aa7ef23",  # 通过 `adb devices` 获取
        # 自动化引擎（Android 必选）
        automationName="UiAutomator2",  # Android 的默认驱动，必须明确指定
        # 超时时间（单位：秒）
        newCommandTimeout=300,  # 300 秒内无新命令则自动关闭会话
    )
    # 初始化驱动
    driver = webdriver.Remote(
        'http://localhost:4723',
        options=UiAutomator2Options().load_capabilities(desired_caps))
    try:
        # 滑动操作 duration 毫秒
        # driver.swipe(start_x=551,start_y=1586,end_x=561,end_y=627,duration=602)
        # scroll 拖拽元素
        element1 = driver.find_element(by=AppiumBy.XPATH, value='//*[@text="WLAN"]')
        element2 = driver.find_element(by=AppiumBy.XPATH, value='//*[@text="显示"]')
        driver.scroll(element2,element1)
        # driver.drag_and_drop(element2,element1)
    except:
        print('error！')
        raise
    driver.quit()


if "__main__" == __name__:
    main()
