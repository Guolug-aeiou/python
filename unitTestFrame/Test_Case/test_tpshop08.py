import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os

from dotenv import load_dotenv

load_dotenv('../../config/Python.env')


class TestTPShop08(unittest.TestCase):
    def test_t12(self):
        print(123)

    def test_login_code_null(self):
        now_time = time.strftime('%Y_%m_%d %H_%M_%S')
        # 打开教务系统
        driver = webdriver.Chrome(service=Service(os.getenv("URL_CHROME")))
        driver.get('http://192.168.110.33/home.aspx')
        driver.maximize_window()
        driver.implicitly_wait(8)
        # 跳转到 ifrom 中登录
        driver.switch_to.frame('frm_login')
        # 输入用户名和密码
        # 不输入验证码后点击登录
        action = ActionChains(driver)
        (action
         .click(driver.find_element(By.ID, 'txt_asmcdefsddsd'))
         .send_keys('admin')
         .click(driver.find_element(By.ID, 'txt_psasas'))
         .send_keys('123456')
         .click(driver.find_element(By.ID, 'btn_login'))
         .perform())
        alert = driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        try:
            # 提示 '须录入验证码！'
            # self.assertEqual(alert_text, '录入验证码！')
            assert alert_text == '录入验证码！'
        except AssertionError as e:
            # 无提示 '须录入验证码！' 进行截图
            driver.get_screenshot_as_file(f'../../image_error/error{now_time}.png')
            raise  # 抛出异常
        driver.quit()


if __name__ == '__main__':
    unittest.main()
