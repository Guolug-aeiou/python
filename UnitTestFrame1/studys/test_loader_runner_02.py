import unittest
def main():
    suite = unittest.TestLoader().discover('../case', 'test_*.py')
    unittest.TextTestRunner().run(suite)

if __name__ == "__main__":
    main()
