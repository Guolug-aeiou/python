from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def get_driver():
    driver = webdriver.Chrome(service=Service(
        r"D:\Application_object\environment\chromeDriver\chromedriver-win64-134.0.6998.36\chromedriver.exe"))
    driver.maximize_window()
    return driver
