from selenium import webdriver
from selenium.webdriver.chrome.service import Service

import os

from dotenv import load_dotenv

load_dotenv('../../../config/Python.env')




class GetDriver:
    driver = None

    # 获取Driver
    @classmethod
    def get_driver(cls):
        # 单例模式
        if cls.driver is None:
            cls.driver = webdriver.Chrome(service=Service(os.getenv("URL_CHROME")))
            cls.driver.get(os.getenv("URL_CALCULATOR"))
            cls.driver.maximize_window()
        return cls.driver

    # 关闭浏览器
    @classmethod
    def quit_driver(cls):
        if cls.driver is not None:
            cls.driver.quit()
            cls.driver = None
