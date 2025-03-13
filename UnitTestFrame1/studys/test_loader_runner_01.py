import unittest

def main():
    # 实例化 套件对象
    suite = unittest.TestLoader().discover('../case', 'test_*.py')
    # 实例化 运行对象
    unittest.TextTestRunner().run(suite)

if __name__ == "__main__":
    main()
