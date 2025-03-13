import unittest
def main():
    unittest.TextTestRunner().run(unittest.TestLoader().discover('../case', 'test_*.py'))
if __name__ == "__main__":
    main()
