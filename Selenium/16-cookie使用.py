from time import sleep
import unittest
from selenium import webdriver
from selenium.webdriver.ie.service import Service


def main():
    driver = webdriver.Chrome(service=Service(
        r'D:\Application_object\environment\chromeDriver\chromedriver-win64-134.0.6998.36\chromedriver.exe'))
    # 给driver 添加 cookie
    driver.get('https://www.baidu.com')
    driver.add_cookie({"name":"BDUSS","value":"VnQUxkSFUtU3Bva3pCT1BZRUVYNEJjM21yRTctfmF3SXFIRWsyckduM2R4UE5uSUFBQUFBJCQAAAAAAQAAAAEAAABcfNY4dHV0b3UyMQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAN03zGfdN8xnTU"})
    driver.refresh()
    sleep(10)

if __name__ == '__main__':
    main()
