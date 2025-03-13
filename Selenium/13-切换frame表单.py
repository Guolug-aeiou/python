from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service


def main():
    # 实例化 驱动对象
    driver = webdriver.Chrome(service=Service(
        r"D:\Application_object\environment\chromeDriver\chromedriver-win64-134.0.6998.36\chromedriver.exe"))
    # 隐式等待
    driver.implicitly_wait(1)
    # 启动浏览器打开被测页面
    driver.get(r'D:\Application_object\project_Python\Selenium\testStyleHTML\注册实例.html')
    # 浏览器放大
    driver.maximize_window()
    # 实例化 ActionChains 启动链式交互
    action = ActionChains(driver)
    # 注册页面填写内容
    sleep(1)
    (action
     .click(driver.find_element(By.ID, 'user'))
     .send_keys('admin')
     .click(driver.find_element(By.ID, 'password'))
     .send_keys('123456')
     .click(driver.find_element(By.ID, 'tel'))
     .send_keys('13415190974')
     .click(driver.find_element(By.ID, 'email'))
     .send_keys('guolug1@126.com')
     .perform())
    # 跳转到 注册A 页面
    driver.switch_to.frame("myframe1")
    # 重置 ActionChains 实例化
    action = ActionChains(driver)
    # 注册A页面填写内容
    (action
     .click(driver.find_element(By.ID, 'userA'))
     .send_keys('admin')
     .click(driver.find_element(By.ID, 'passwordA'))
     .send_keys('123456')
     .click(driver.find_element(By.ID, 'telA'))
     .send_keys('13415190974')
     .click(driver.find_element(By.ID, 'emailA'))
     .send_keys('guolug1@126.com')
     .perform())
    # 恢复默认页面后 跳转到 注册B 页面
    driver.switch_to.default_content()
    driver.switch_to.frame("myframe2")
    # 重置 ActionChains 实例化
    action = ActionChains(driver)
    # 注册B页面填写内容
    (action
     .click(driver.find_element(By.ID, 'userB'))
     .send_keys('admin')
     .click(driver.find_element(By.ID, 'passwordB'))
     .send_keys('123456')
     .click(driver.find_element(By.ID, 'telB'))
     .send_keys('13415190974')
     .click(driver.find_element(By.ID, 'emailB'))
     .send_keys('guolug1@126.com')
     .perform())

if __name__ == '__main__':
    main()
