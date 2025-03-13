from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service


def main():
    driver = webdriver.Chrome(service=Service(
        r"D:\Application_object\environment\chromeDriver\chromedriver-win64-134.0.6998.36\chromedriver.exe"))
    # 打开被测页面
    driver.get(r'D:\Application_object\project_Python\Selenium\testStyleHTML\select.html')
    # 放大窗口
    driver.maximize_window()
    # 隐式等待无效
    driver.find_element(By.ID,'talert').click()
    alert  = driver.switch_to.alert
    print(alert.text)
    alert.dismiss()
    sleep(5)

if __name__ == "__main__":
    main()
