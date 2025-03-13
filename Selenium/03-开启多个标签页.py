from time import sleep

from tools.driverchrome.init_chrome_driver import get_driver


def main():
    driver = get_driver()
    driver.get('https://www.baidu.com')
    # 开第二个窗口（新标签页）
    driver.maximize_window()
    driver.execute_script("window.open()")
    sleep(3)
    # 切换到新窗口（注意：此时还在第一个窗口！）
    driver.switch_to.window(driver.window_handles[1])
    driver.get('https://www.baidu.com')
    sleep(1)
    driver.execute_script("window.open()")
    sleep(1)
    driver.close()
    sleep(3)


if __name__ == '__main__':
    main()
