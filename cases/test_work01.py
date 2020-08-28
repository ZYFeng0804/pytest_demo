import time
import allure
import pytest

import config
from base.base_driver import BaseDriver
from handle.home_handle import HomeHandle
from handle.login_handle import LoginHandle
from utils import json2list


def build_data():
    """ 参数化构造方法 """
    filepath = config.BASE_DIR + "/data/login_data.json"
    keylist = ["username", "password", "veriycode", "dialog_text"]
    return json2list(filepath, keylist)


@allure.feature("登录页面")
class TestLogin:
    mydriver = None
    homepage = None
    loginpage = None

    def setup_class(self):
        self.mydriver = BaseDriver('http://localhost/')
        self.mydriver.set_max_window()
        self.mydriver.set_imp_wait(10)

    def teardown_class(self):
        time.sleep(2)
        self.mydriver.quit()

    # @pytest.mark.skip
    @allure.title('进入主页后跳转至登录页')
    @pytest.mark.run(order=1)
    def test_to_loginpage(self):
        self.homepage = HomeHandle(self.mydriver)
        self.homepage.go_2_loginpage()

    # @pytest.mark.skip
    @allure.title("登录")
    @allure.description("用例描述：测试登录的各种异常情况")
    @pytest.mark.parametrize(("username", "password", "veriycode", "dialog_text"), build_data())
    @pytest.mark.run(order=2)
    def test_login_error(self, username, password, veriycode, dialog_text):
        self.loginpage = LoginHandle(self.mydriver)
        self.loginpage.input_username(username)
        self.loginpage.input_password(password)
        self.loginpage.input_veriycode(veriycode)
        self.loginpage.click_login()
        dialog_text = self.loginpage.get_dialog_text()
        time.sleep(1)
        self.loginpage.click_dialog_yes_bg()
        assert dialog_text == dialog_text
