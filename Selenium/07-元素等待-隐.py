from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def main():
    # 实例化驱动
    driver = webdriver.Chrome(service=Service(
        r"D:\Application_object\environment\chromeDriver\chromedriver-win64-134.0.6998.36\chromedriver.exe"))
    # 设置隐式等待
    driver.implicitly_wait(10)
    # 打开地址
    driver.get("https://www.baidu.com")
    # 最大化
    driver.maximize_window()
    # 寻找元素
    (ActionChains(driver)
     .click(driver.find_element(By.CSS_SELECTOR, 'div>div>div>div.tool_3HMbZ')))

    sleep(20)


if __name__ == '__main__':
    main()
