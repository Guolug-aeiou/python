import unittest
from time import sleep

from unitTestFrame.module.add import add


class TestCaseAssert06(unittest.TestCase):
    def test_add_1(self):
        self.assertTrue(add(1, 0) == 1)

    def test_add_2(self):
        self.assertTrue(add(1, 1) == 2)

    def test_add_3(self):
        self.assertTrue(add(1, 2) == 3)

    def test_add_4(self):
        self.assertTrue(add(1, 3) == 4)

    def test_add_5(self):
        self.assertTrue(add(5, 0) == 5)

    def test_add_6(self):
        self.assertFalse(add(5, 0) == 0)

if __name__ == '__main__':
    unittest.main()
