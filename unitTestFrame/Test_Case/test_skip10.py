import unittest

from unitTestFrame.module.add import add


# @unittest.skip("测试skip的使用")
class TestParm09(unittest.TestCase):
    @unittest.skip("测试skip的使用")
    def test_add_1(self):
        print(add(1, 3))

    def test_add_2(self):
        print(add(1, 3))

    @unittest.skipIf(1 + 1 == 2, "测试skipIf的使用")
    def test_add_3(self):
        print(add(1, 3))


if __name__ == '__main__':
    unittest.main()
