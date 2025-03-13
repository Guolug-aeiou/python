from time import sleep

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from tools.driverchrome.init_chrome_driver import get_driver


def main():
    driver = get_driver()
    driver.get('https://www.baidu.com')
    action = ActionChains(driver)
    # 实现复制功能
    (action
     .click(driver.find_element(By.CSS_SELECTOR, '#kw'))
     .send_keys('test')
     .key_down(Keys.CONTROL)
     .send_keys('a')
     .key_up(Keys.CONTROL)
     .perform())
    sleep(10)

if __name__ == '__main__':
    main()
