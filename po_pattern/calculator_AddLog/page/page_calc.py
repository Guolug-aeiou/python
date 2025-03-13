from selenium.webdriver.common.by import By

from po_pattern.calculator_AddLog import page
from po_pattern.calculator_AddLog.base.base import Base


class PageCalc(Base):
    # 点击数字
    def page_click_number(self, num):
        for i in str(num):
            self.base_click((By.ID, f"simple{i}"))

    # 点击加号
    def page_click_add(self):
        self.base_click(page.SIMPLEADD)

    # 点击等号
    def page_click_equal(self):
        self.base_click(page.SIMPLEEQUAL)

    # 获取结果
    def page_get_value(self):
        return self.base_get_value(page.RESULTIPT)

    # 点击clear
    def page_click_clear(self):
        self.base_click(page.SIMPLECLEARALLBTN)

    # 组装
    def page_add_group(self, num1, num2):
        self.page_click_clear()
        self.page_click_number(num1)
        self.page_click_add()
        self.page_click_number(num2)
        self.page_click_equal()
        return self.page_get_value()