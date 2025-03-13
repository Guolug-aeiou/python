"""

"""
def main():
    # 1,导包
    import unittest

    from UnitTestFrame.studys.test_Demo1 import TestDemo1
    from UnitTestFrame.studys.test_Demo2 import TestDemo2

    # 2,实例化套件对象
    suite = unittest.TestSuite()
    # 3,使用套件对象添加用例方法
    # 方式一
    suite.addTest(TestDemo1('test_method1'))
    suite.addTest(TestDemo1('test_method2'))
    suite.addTest(TestDemo2('test_method1'))
    suite.addTest(TestDemo2('test_method2'))
    # 方式二
    suite.addTest(unittest.makeSuite(TestDemo1))
    suite.addTest(unittest.makeSuite(TestDemo2))
    # 4,实例化运行对象
    runner = unittest.TextTestRunner()
    # 5,使用运行对象去执行套件对象
    runner.run(suite)
if __name__ == '__main__':
    main()