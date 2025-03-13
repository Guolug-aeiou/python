import unittest

from parameterized import parameterized

from po_pattern.V1.page.page_login import PageLogin


def get_data():
    return [('test', '123456', '用户名或密码有误，请重新输入或找回密码'),
            ('admin', '123456', 'msg')]


class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 启动浏览器
        cls.login = PageLogin()
        cls.login.page_click_login_link()
    @classmethod
    def tearDownClass(cls):
        # 关闭浏览器
        cls.login.driver.quit()

    @parameterized.expand(get_data())
    def test_login(self, name, password, login_result_msg):
        # 调用 page_login_group1
        self.login.page_login_group(name, password)
        # 登录信息
        msg = self.login.page_get_message()
        try:
            # 断言
            self.assertEqual(msg, login_result_msg)
        except AssertionError as e:
            # 截图
            self.login.page_get_image(r'D:/Application_object/project_Python/po_pattern/V1/image_test_message')
            raise e
