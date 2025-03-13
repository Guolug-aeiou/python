# 1,导包 unittest /par..
import json
import unittest
from parameterized import parameterized
from UnitTestFrame.Login_module.login import login


# 4,组织测试数据并传参
def build_data() -> list:
    with open('data.json', 'r', encoding='utf-8') as f:
        data = []
        result = json.load(f)
        for temp in result:
            data.append((temp.get('username'), temp.get('password'), temp.get('expect')))
    return data


# 2,定义测试类
class TestLogin(unittest.TestCase):
    # 3.书写测试方法(测试数据用变量代替)
    @parameterized.expand(build_data())
    def test_login(self, username, password, expect):
        self.assertEquals(expect, login(username, password))
