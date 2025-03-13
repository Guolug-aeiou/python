import unittest

from UnitTestFrame.Login_module.login import login


class test_assert_login(unittest.TestCase):
    def test_login_userName_error_password_normal(self):
        self.assertEquals('您输入的用户名或密码错误!', login('admin1', '123456'))

    def test_login_password_error_username_normal(self):
        self.assertEquals('您输入的用户名或密码错误!', login('123456', '123456'))

    def test_login_password_username_error(self):
        self.assertEquals('您输入的用户名或密码错误!', login('12345612', 'weqdqw'))

    def test_login_password_username_normal(self):
        self.assertEquals('登录成功!', login('admin1', '123456'))
