import subprocess

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import platform


def run_shell_get_output(order1, order2):
    """
        @order1 = 命令
        @order2 = 命令参数
        @return = 命令执行结果
    """
    # 运行命令并捕获输出
    command = [order1] + order2.split()
    result = subprocess.run(args=command, capture_output=True, text=True)
    '''
    self.result = subprocess.run(["echo", "Hello, World!"], capture_output=True, text=True)
    '''
    # 打印命令的输出
    return "/*" * 20 + "/" + "\nOutput:" + result.stdout


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
