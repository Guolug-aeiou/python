# 导入包
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def main():
    # 实例化 driver
    driver = webdriver.Chrome(service=Service(
        r"D:\Application_object\environment\chromeDriver\chromedriver-win64-134.0.6998.36\chromedriver.exe"))
    # 打开浏览器进入被测页面
    driver.get(r'D:\Application_object\project_Python\Selenium\testStyleHTML\select.html')
    # 获取到元素
    el = driver.find_element(By.ID,'Tselect')
    # 切换 上海
    sleep(2)
    Select(el).select_by_index(1)
    # 切换 广州
    sleep(2)
    Select(el).select_by_value('gz')
    # 切换 汕头
    sleep(2)
    Select(el).select_by_visible_text('汕头')
    # 切换 北京
    sleep(2)
    Select(el).select_by_index(0)

if __name__ == '__main__':
    main()
