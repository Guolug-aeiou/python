from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service


def main():
    # 实例化 驱动
    driver = webdriver.Chrome(service=Service(
        r'D:\Application_object\environment\chromeDriver\chromedriver-win64-134.0.6998.36\chromedriver.exe'))
    # 浏览器打开被测页面
    driver.get(r'D:\Application_object\project_Python\Selenium\testStyleHTML\注册实例.html')
    driver.maximize_window()
    # 获取当前页面句柄
    current_handle = driver.current_window_handle
    sleep(2)
    # 点击注册页面A
    driver.find_element(By.ID, 'ZCA').click()
    # 获取当前都有窗口的句柄
    for handle in driver.window_handles:
        if handle != current_handle:
            # 切换到handle句柄的页面中
            driver.switch_to.window(handle)
            sleep(2)
            # 输入注册信息
            action = ActionChains(driver)
            (action
             .click(driver.find_element(By.ID, 'userA'))
             .send_keys('admin')
             .click(driver.find_element(By.ID, 'passwordA'))
             .send_keys('123456')
             .perform())
    sleep(5)


if __name__ == '__main__':
    main()
