from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service
def main():
    sleep_time=1
    user = '13415190974'
    password = 'xxtGuo001215.'
    # 实例化驱动并指定位置
    driver = webdriver.Chrome(service=Service(r"D:\Application_object\environment\chromeDriver\chromedriver-win64-134.0.6998.36\chromedriver.exe"))
    # 打开浏览器
    driver.get('https://i.chaoxing.com/')
    # 窗口最大化
    driver.maximize_window()
    # 获取当前页面的URL
    print(driver.current_url)
    # 输入用户名
    element_user = driver.find_element(By.CSS_SELECTOR, 'form>div>input.ipt-tel[placeholder="手机号/超星号"]')
    element_user.clear()
    element_user.click()
    element_user.send_keys(user)
    # 输入密码
    element_password = driver.find_element(By.CSS_SELECTOR, 'form>div>input.ipt-pwd[placeholder="学习通密码"]')
    element_password.clear()
    element_password.click()
    element_password.send_keys(password)
    # 点击登录
    element_login = driver.find_element(By.CSS_SELECTOR,'div>button[type="button"].btn-big-blue.margin-btm24')
    element_login.click()
    sleep(sleep_time)
    # 退回 到第一个页面
    driver.back()
    sleep(sleep_time)
    # 前进 到第二个页面
    driver.forward()
    sleep(sleep_time)
    # 设置窗口大小
    driver.set_window_size(700,700)
    # 设置窗口显示位置
    driver.set_window_position(600,500)
    sleep(sleep_time)
    driver.switch_to.window(driver.window_handles[0])
    sleep(sleep_time)
    # 关闭浏览器
    driver.quit()


if __name__ == '__main__':
    main()
