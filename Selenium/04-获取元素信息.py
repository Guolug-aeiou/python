from time import sleep

from selenium.webdriver.common.by import By

from a_tools.driverchrome.init_chrome_driver import get_driver


def main():
    driver = get_driver()
    driver.get('https://www.baidu.com')
    element = driver.find_element(By.CSS_SELECTOR,'span>input.bg.s_btn#su')
    # 获取元素的大小
    print(element.size)
    # 获取元素的内容
    print(element.text) # 有时会获取不到内容
    # 获取元素的属性
    print(element.get_attribute('value'))
    print(element.get_attribute('type'))
    # 是否可见
    print(element.is_displayed())
    # 是否选中
    print(element.is_selected())
    # 是否可用
    print(element.is_enabled())
    sleep(10)
    driver.quit()

if __name__ == '__main__':
    main()