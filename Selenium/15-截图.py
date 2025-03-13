import datetime
import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.ie.service import Service


def main():
    driver = webdriver.Chrome(service=Service(
        r'D:\Application_object\environment\chromeDriver\chromedriver-win64-134.0.6998.36\chromedriver.exe'))
    driver.get(r'D:\Application_object\project_Python\Selenium\testStyleHTML\注册实例.html')
    driver.maximize_window()
    sleep(2)
    now_time = time.strftime('%Y_%m_%d %H_%M_%S')
    driver.get_screenshot_as_file(f'./images/注册实{now_time}.png')


if __name__ == '__main__':
    main()
