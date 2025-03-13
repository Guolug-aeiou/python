import unittest

from UnitTestFrame1.studys.tools import add


class test_tools_add(unittest.TestCase):
    # 夹具
    def setUp(self):
        print('方法执行前会执行...')
    def tearDown(self):
        print('方法执行后会执行...\n')
    @classmethod
    def setUpClass(cls):
        print('类执行前会执行...')
    @classmethod
    def tearDownClass(cls):
        print('类执行后会执行...')

    def test_method1(self):
        if add(1, 2) == 3:
            print(self)
            print('测试通过!')
        else:
            print('测试不通过!')

    def test_method2(self):
        if add(10, 20) == 30:
            print(self)
            print('测试通过!')
        else:
            print('测试不通过!')
    def test_method3(self):
        if add(1000, 2000) == 3000:
            print(self)
            print('测试通过!')
        else:
            print('测试不通过!')

    def test_method4(self):
        if add(5, 9) == 14:
            print(self)
            print('测试通过!')
        else:
            print('测试不通过!')