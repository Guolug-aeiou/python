# 1,导包 unittest /par..
import unittest
version =30
# 2,定义测试类
class TestLogin(unittest.TestCase):
    @unittest.skip("没有原因就是想跳过")
    def test_login_01(self):
        print('测试1')
    @unittest.skipIf(version <= 40,'版本 <= 40 则跳过')
    def test_login_02(self):
        print('测试2')
    def test_login_03(self):
        print('测试3')
    def test_login_04(self):
        print('测试4')