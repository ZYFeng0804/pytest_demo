from base.base_handle import BaseHandle
from page.login_page import LoginPage


class LoginHandle(BaseHandle):
    """ 登录页操作类 """

    def __init__(self, driver):
        self.driver = driver
        self.login_model = LoginPage()

    def input_username(self, username):
        """ 输入账号 """
        element = self.driver.get_element(self.login_model.get_username_id())
        self.input_text(element, username)

    def input_password(self, pwd):
        """ 输入密码 """
        element = self.driver.get_element(self.login_model.get_password_id())
        self.input_text(element, pwd)

    def input_veriycode(self, code):
        """ 输入验证码 """
        element = self.driver.get_element(self.login_model.get_veriycode_id())
        self.input_text(element, code)

    def click_login(self):
        """ 点击登录 """
        element = self.driver.get_element(self.login_model.get_login_bt_name())
        self.click_element(element)

    def get_dialog_text(self):
        """ 获取天窗信息 """
        element = self.driver.get_element(self.login_model.get_dialog_text_cls_name())
        return self.get_text(element)

    def click_dialog_yes_bg(self):
        """ 点击天窗确定按钮 """
        element = self.driver.get_element(self.login_model.get_dialog_yes_bt_link())
        self.click_element(element)
