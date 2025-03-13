import unittest
from parameterized import parameterized


def get_data():
    return [(1, 2, 3),
            (2, 4, 6),
            (3, 4, 7),
            (3, 4, 7),
            (3, 4, 7),
            (3, 4, 7),
            (1, 4, 5),
            (1, 4, 5)]


class TestParm09(unittest.TestCase):
    @parameterized.expand([(1, 3, 4)])
    def test_add_1(self, a, b, result):
        print(f'{a}+{b}={result}')
    @parameterized.expand(get_data())
    def test_add_2(self,a,b,result):
        print(f'{a}+{b}={result}')

if __name__ == '__main__':
    unittest.main()
