from time import sleep

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait


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
    # 设置隐式等待 20 密码
    driver.implicitly_wait(20)
    try:
        # 回到 home 页面
        driver.start_activity('com.miui.home', 'com.miui.home.launcher.Launcher')
        # 点击设置
        driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ImageView[@content-desc="设置"]').click()
        # 获取一组元素
        element_list = driver.find_elements(by=AppiumBy.XPATH, value='//*[@resource-id="android:id/title"]')
        print("点击了")
        print(len(element_list))
        for i in element_list:
            print(i.text)
        element_list[0].click()
        # 设置显式等待
        (WebDriverWait(driver, timeout=20, poll_frequency=0.5).until(
            lambda x: x.find_element(by=AppiumBy.XPATH, value='//*[@class="miui.widget.ClearableEditText"]'))
         .send_keys("hello"))
    except Exception as e:
        print("=" * 40)
        print(e)
        print("=" * 40)
    driver.quit()


if "__main__" == __name__:
    main()
