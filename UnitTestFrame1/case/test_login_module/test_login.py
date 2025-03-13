# 1,导包 unittest /par..
import unittest

from parameterized import parameterized

from UnitTestFrame.Login_module.login import login

# 4,组织测试数据并传参
data = [
    ('admin', '123456', '登录成功!'),
    ('admin1', '123456', '登录失败!'),
    ('admin', '1123456', '登录失败!')
]


# 2,定义测试类
class TestLogin(unittest.TestCase):
    # 3.书写测试方法(测试数据用变量代替)
    @parameterized.expand(data)
    def test_login(self,username, password, expect):
        self.assertEquals(expect, login(username, password))
