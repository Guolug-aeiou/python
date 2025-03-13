import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.ie.service import Service
from selenium.webdriver.support.wait import WebDriverWait
import os
from dotenv import load_dotenv

load_dotenv('../../../config/Python.env')


class Base:
    # 初始化
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(os.getenv("URL_CHROME")))
        self.driver.get('https://www.baidu.com')
        self.driver.maximize_window()

    # 查找元素方法
    def base_find_element(self, loc: tuple, timeout=30, poll=0.5):
        # 显式等待
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 点击方法
    def base_click(self, loc: tuple,head_sleep_time=0):
        sleep(head_sleep_time)
        self.base_find_element(loc).click()

    # 输入方法
    def base_sends_keys(self, loc: tuple, value: str,head_sleep_time=0):
        sleep(head_sleep_time)
        el = self.base_find_element(loc)
        el.clear()
        el.send_keys(value)

    # 获取文本方法
    def base_get_text(self, loc: tuple,head_sleep_time=0) -> str:
        sleep(head_sleep_time)
        return self.base_find_element(loc).text

    # 截图方法
    def base_get_screenshot_as_file(self, path: str,head_sleep_time=0):
        sleep(head_sleep_time)
        self.driver.get_screenshot_as_file(fr'{path}/{time.strftime('%Y_%m_%d %H_%M_%S')}.png')
