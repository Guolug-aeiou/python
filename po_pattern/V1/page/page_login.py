from po_pattern.V1 import page
from po_pattern.V1.base.base import Base


class PageLogin(Base):
    # 点击登录链接
    def page_click_login_link(self):
        self.base_click(page.LOGIN_link)

    # 输入用户名
    def page_send_keys_username(self, name: str):
        self.base_sends_keys(page.LOGIN_username, name)

    # 输入密码
    def page_send_keys_password(self, password: str):
        self.base_sends_keys(page.LOGIN_password, password)

    # 点击同意协议
    def page_click_agree(self):
        self.base_click(page.LOGIN_agree)

    # 点击登录
    def page_click_login_btn(self):
        self.base_click(page.LOGIN_btn)

    # 获取异常信息
    def page_get_message(self) -> str:
        return self.base_get_text(page.LOGIN_message, head_sleep_time=0.5)

    # 截图
    def page_get_image(self, path: str):
        self.base_get_screenshot_as_file(path)

    # 组合业务
    def page_login_group(self, name: str, password: str):
        self.page_send_keys_username(name)
        self.page_send_keys_password(password)
        self.page_click_agree()
        self.page_click_login_btn()
