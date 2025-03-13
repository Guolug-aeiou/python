import time
from pathlib import Path

from selenium.webdriver.support.wait import WebDriverWait

from a_tools.logging_format.logger_factory import LoggerFactory


class Base:
    def __init__(self, driver):
        self.logger = LoggerFactory.get_logger(
            name="Test_add",
            level="DEBUG",
            log_file=Path(__file__).parent / "../log/Test_add.log",
        )
        self.driver = driver

    # 查找元素
    def base_find_element(self, loc: tuple, timeout=30, poll=0.5):
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 点击
    def base_click(self, loc: tuple):
        self.base_find_element(loc).click()

    # 输入
    def base_send_keys(self, loc: tuple, value: str):
        self.base_find_element(loc).send_key(value)

    # 获取内容
    def base_get_value(self, loc: tuple) -> str:
        return self.base_find_element(loc).get_attribute('value')

    # 截图
    def base_get_image(self, path: str, head_sleep_time=0):
        time.sleep(head_sleep_time)
        self.driver.get_screenshot_as_file(fr'{path}/{time.strftime('%Y_%m_%d %H_%M_%S')}.png')

    # 判断元素是否存在
    def base_is_element_exist(self, loc: tuple):
        try:
            self.base_find_element(loc, timeout=2)
            return True
        except:
            return False
