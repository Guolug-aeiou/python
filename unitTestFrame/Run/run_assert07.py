import unittest


def main():
    unittest.TextTestRunner().run(unittest.TestLoader().discover('../Test_Case','test*assert*.py'))


if __name__ == '__main__':
    main()
