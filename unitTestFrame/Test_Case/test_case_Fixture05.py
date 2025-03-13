import unittest

from unitTestFrame.module.add import add


class TestCaseFixture05(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('<' + '-' * 20 + '⬇' + '-' * 20 + '>')

        print('调用本类方法时首先会执行一次！')

    @classmethod
    def tearDownClass(cls):
        print('调用本类方法结束后会执行一次！')
        print('<' + '-' * 20 + '⬆' + '-' * 20 + '>')

    def setUp(self):
        print('<' + '-' * 10 + '⬇' + '-' * 10 + '>')
        print('调用每个方法时会先执行本方法！')

    def tearDown(self):
        print('调用每个方法后会执行本方法！')
        print('<' + '-' * 10 + '⬆' + '-' * 10 + '>')

    def test_add_1(self):
        print(bool(add(1, 0) == 1))

    def test_add_2(self):
        print(bool(add(1, 1) == 2))

    def test_add_3(self):
        print(bool(add(1, 2) == 3))

    def test_add_4(self):
        print(bool(add(1, 3) == 4))

    def test_add_5(self):
        print(bool(add(1, 4) == 5))


if __name__ == '__main__':
    unittest.main()
