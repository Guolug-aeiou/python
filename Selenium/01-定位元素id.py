from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


def main():
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com')
    element_kw = driver.find_element(By.XPATH,"//input[@id='kw']")
    element_kw.click()
    element_kw.send_keys('123456')
    element_su = driver.find_element(By.XPATH,"//input[@id='su']")
    element_su.click()
    sleep(2)
    driver.find_element(By.CSS_SELECTOR,'body a .index-logo-src').click()
    sleep(2)


if __name__ == '__main__':
    main()
