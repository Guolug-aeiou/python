import unittest

from parameterized import parameterized

from po_pattern.calculator.base.get_driver import GetDriver
from po_pattern.calculator.page.page_calc import PageCalc
from po_pattern.calculator.scripts.test import get_param


class TestAdd(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.calc = PageCalc(GetDriver.get_driver())

    @classmethod
    def tearDownClass(cls):
        GetDriver.quit_driver()

    @parameterized.expand(get_param())
    def test_add(self, num1, num2, expect):
        try:
            self.assertEqual(int(self.calc.page_add_group(num1, num2)), expect)
        except Exception as e:
            # 截图
            self.calc.base_get_image(r'D:\Application_object\project_Python\po_pattern\calculator\image_test_msg')
            raise e
