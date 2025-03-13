import unittest
from pathlib import Path

from parameterized import parameterized

from a_tools.logging_format.logger_factory import LoggerFactory
from po_pattern.calculator.base.get_driver import GetDriver
from po_pattern.calculator.page.page_calc import PageCalc
from po_pattern.calculator.scripts.test import get_param

# 获取日志对象（单例模式）
logger = LoggerFactory.get_logger(
    name="Test_add",
    level="DEBUG",
    log_file=Path(__file__).parent / "app.log",
)


class TestAdd(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.calc = PageCalc(GetDriver.get_driver())
        logger.debug("This is a debug message")

    @classmethod
    def tearDownClass(cls):
        GetDriver.quit_driver()
        logger.info("This is an info message")

    @parameterized.expand(get_param())
    def test_add(self, num1, num2, expect):
        logger.warning("This is a 警告 message")
        logger.error("This is an error message")
        logger.critical("This is a critical message")
        try:
            self.assertEqual(int(self.calc.page_add_group(num1, num2)), expect)
        except Exception as e:
            # 截图
            self.calc.base_get_image(r'D:\Application_object\project_Python\po_pattern\calculator\image_test_msg')
            raise e
