import unittest

from unitTestFrame.Test_Case.test_case01 import TestCase01


def main():
    # 实例化 TestSuite
    suite = unittest.TestSuite()
    # 实例化 makeSuite 添加测试用例扩展
    suite.addTest(unittest.makeSuite(TestCase01))
    # 实例化 TextTestRunner
    unittest.TextTestRunner().run(suite)

if __name__ == '__main__':
    unittest.main()
