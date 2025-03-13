import unittest

from UnitTestFrame.case.test_tools_add import test_tools_add

def main():
    # 实例化 套件对象(套件对象是将多个用例添加到-提测表-)
    suite = unittest.TestSuite()
    # 将测试用例添加到套件中
    suite.addTest(test_tools_add('test_method1'))
    suite.addTest(test_tools_add('test_method2'))
    suite.addTest(test_tools_add('test_method3'))
    suite.addTest(test_tools_add('test_method4'))
    # 实例化 运行对象(运行对象是将-提测表-的用例运行)
    unittest.TextTestRunner().run(suite)
if __name__ == "__main__":
    main()
