from base.base_handle import BaseHandle
from page.home_page import HomePage


class HomeHandle(BaseHandle):
    """ 主页操作类 """

    def __init__(self, driver):
        self.driver = driver
        self.home_model = HomePage()

    def go_2_loginpage(self):
        """ 进入登录页 """
        element = self.driver.get_element(self.home_model.loginpage_cls_name())
        self.click_element(element)
