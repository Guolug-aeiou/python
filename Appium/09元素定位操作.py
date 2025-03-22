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
        # # 打开超星学习通
        # driver.start_activity('com.chaoxing.mobile', '.main.ui.MainTabActivity')
        # 找到 设置按钮 元素
        sleep(2)
        elt_me_sz = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ImageView[@content-desc="设置"]')
        # elt_me_sz = driver.find_element(By.XPATH,'//android.widget.ImageView[@content-desc="设置"]')
        elt_me_sz.click()
        sleep(3)
        elt_me_ss = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@content-desc="搜索"]')
        # elt_me_ss = driver.find_element(By.XPATH,'//android.widget.TextView[@content-desc="搜索"]')
        elt_me_ss.click()
        sleep(3)
        # 获取输入框
        elt_me_et = driver.find_element(by=AppiumBy.ID,value='android:id/input')
        elt_me_et.click()
        sleep(2)
        elt_me_et.send_keys("hello")
        print("点击了")
    except:
        print('出错了')
    driver.quit()


if "__main__" == __name__:
    main()
