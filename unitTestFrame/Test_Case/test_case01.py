import unittest

from unitTestFrame.module.add import add


class TestCase01(unittest.TestCase):
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