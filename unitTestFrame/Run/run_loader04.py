import unittest


def main():
    # TestLoader() 和 defaultTestLoader效果一样
    unittest.TextTestRunner().run(unittest.TestLoader().discover('../Test_Case','test*.py'))
    unittest.TextTestRunner().run(unittest.defaultTestLoader.discover('../Test_Case','test*.py'))

if __name__ == '__main__':
    main()
