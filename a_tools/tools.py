from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import platform


def paste_text(driver, element):
    """通用粘贴方法"""
    # 强制聚焦
    driver.execute_script("arguments[0].select();", element)

    # 判断操作系统
    modifier = Keys.COMMAND if platform.system() == 'Darwin' else Keys.CONTROL

    # 执行粘贴
    (ActionChains(driver)
     .key_down(modifier)
     .send_keys('v')
     .key_up(modifier)
     .perform())
