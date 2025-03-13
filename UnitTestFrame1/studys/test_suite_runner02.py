import unittest
from UnitTestFrame.case.test_login_module.test_assert_login import test_assert_login
from UnitTestFrame.case.test_tools_add import test_tools_add
from UnitTestFrame.case.test_Demo1 import test_demo_1

# 实例化套件对象
suite = unittest.TestSuite()
# 将 case 装载到套件中
suite.addTest(test_assert_login('test_login_userName_error_password_normal'))
suite.addTest(test_assert_login('test_login_password_error_username_normal'))
suite.addTest(test_assert_login('test_login_password_username_error'))
suite.addTest(test_assert_login('test_login_password_username_normal'))
suite.addTest(test_tools_add('test_method1'))
# 实例化运行对象
unittest.TextTestRunner().run(suite)
