from time import sleep

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy


def main():
    desired_caps = dict(
        platformName="Android",
        platformVersion="9",  # 通过 adb 获取
        deviceName="MI 6",  # 设备实际型号
        noReset=True,  # 避免每次启动时重置应用
        uuid="2aa7ef23",
        automationName="UiAutomator2",
        newCommandTimeout=300  # 设置会话超时时间为 300 秒
    )
    driver = webdriver.Remote('http://localhost:4723',
                              options=UiAutomator2Options().load_capabilities(desired_caps))
    try:
        # # 回到 home 页面
        # driver.start_activity('com.miui.home','com.miui.home.launcher.Launcher')
        # # 点击设置
        # driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ImageView[@content-desc="设置"]').click()
        # # 获取一组元素
        # element_list = driver.find_elements(by=AppiumBy.XPATH,value='//*[@resource-id="android:id/title"]')
        # print("点击了")
        # print(len(element_list))
        # for i in element_list:
        #     print(i.text)
        # element_list[0].click()

        element_list2 = driver.find_elements(by=AppiumBy.XPATH,value='//*[@class="miui.widget.ClearableEditText"]')
        print(len(element_list2))
        for i in element_list2:
            print(i)
        element_list2[0].send_keys("hello")
    except Exception as e:
        print("="*40)
        print(e)
        print("=" * 40)
    driver.quit()

if "__main__" == __name__:
    main()
