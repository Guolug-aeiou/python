import unittest

from unitTestFrame.Test_Case.test_case01 import TestCase01


def main():
    # 实例化 TestSuite
    suite = unittest.TestSuite()
    # 添加测试用例
    suite.addTest(TestCase01('test_add_1'))
    suite.addTest(TestCase01('test_add_2'))
    suite.addTest(TestCase01('test_add_3'))
    suite.addTest(TestCase01('test_add_4'))
    suite.addTest(TestCase01('test_add_5'))
    # 实例化执行动作
    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    unittest.main()
