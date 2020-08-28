from selenium.webdriver.common.by import By


class LoginPage(object):
    """ 登录模块模型 """

    def __init__(self):
        self.__username_datas = (By.ID, 'username')
        self.__password_datas = (By.ID, 'password')
        self.__veriycode_datas = (By.ID, 'verify_code')
        self.__login_button_datas = (By.NAME, 'sbtbutton')
        self.__login_dialog_datas = (By.CLASS_NAME, 'layui-layer-content ')
        self.__login_yes_datas = (By.LINK_TEXT, '确定')

    def get_username_id(self):
        """ 账号输入框元素 """
        return self.__username_datas

    def get_password_id(self):
        """ 密码输入框元素 """
        return self.__password_datas

    def get_veriycode_id(self):
        """ 验证码输入框元素 """
        return self.__veriycode_datas

    def get_login_bt_name(self):
        """ 登录按钮元素 """
        return self.__login_button_datas

    def get_dialog_text_cls_name(self):
        """ 获取弹窗信息 """
        return self.__login_dialog_datas

    def get_dialog_yes_bt_link(self):
        """" 获取弹窗确定按钮 """
        return self.__login_yes_datas
