import unittest
from parameterized import parameterized
from po_pattern.calculator_AddLog.base.get_driver import GetDriver
from po_pattern.calculator_AddLog.page.page_calc import PageCalc
from po_pattern.calculator_AddLog.scripts.test import get_param


class TestAdd(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.calc = PageCalc(GetDriver.get_driver())
        cls.calc.logger.info('创建实例化 driver')

    @classmethod
    def tearDownClass(cls):
        GetDriver.quit_driver()
        cls.calc.logger.info('关闭 driver')

    @parameterized.expand(get_param())
    def test_add(self, num1, num2, expect):
        try:
            self.assertEqual(int(self.calc.page_add_group(num1, num2)), expect)
            self.calc.logger.info(f'执行-{num1}+{num2}={expect}-通过！')
        except Exception as e:
            # 截图
            self.calc.base_get_image(r'D:\Application_object\project_Python\po_pattern\calculator_AddLog\image_test_msg')
            self.calc.logger.info(f'执行-{num1}+{num2}={expect}-不通过！截图')
            raise e
