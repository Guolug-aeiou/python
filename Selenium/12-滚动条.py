from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service
def main():
    # 实例化驱动并指定位置
    driver = webdriver.Chrome(service=Service(r"D:\Application_object\environment\chromeDriver\chromedriver-win64-134.0.6998.36\chromedriver.exe"))
    # 打开浏览器
    driver.get(r'D:\Application_object\project_Python\Selenium\testStyleHTML\注册A.html')
    # 窗口最大化
    driver.maximize_window()
    # 获取当前页面的URL
    print(driver.current_url)
    # 滚动条滚动，直接执行 javaScript 脚本
    driver.execute_script('window.scrollTo(0,10000)')
    sleep(5)
    # 关闭浏览器
    driver.quit()

if __name__ == '__main__':
    main()
