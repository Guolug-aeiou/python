from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service
from selenium.webdriver.support.wait import WebDriverWait


def main():
    # 创建实例化
    driver = (webdriver.Chrome(service=Service(
        r"D:\Application_object\environment\chromeDriver\chromedriver-win64-134.0.6998.36\chromedriver.exe")))
    driver.get('https://www.baidu.com')
    # 浏览器放大
    driver.maximize_window()
    # 显式等待元素
    element = WebDriverWait(driver,timeout=10,poll_frequency=0.1).until(lambda x:x.find_element(By.CSS_SELECTOR,'#tset'))
    element.send_keys('test')
    sleep(10)


if __name__ == '__main__':
    main()
