# 1,导包
import unittest
# 2,自定义测试类
class TestDemo1(unittest.TestCase):
    # 3,书写测试方法
    # 测试方法必须以 test_ 开头(本质是test开头)
    def test_method1(self):
        print('测试用例:GB-1-01执行!')
    def test_method2(self):
        print('测试用例:GB-1-02执行!')

# 4,执行测试用例
if __name__ == '__main__':
    TestDemo1()
