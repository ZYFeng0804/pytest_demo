from selenium.webdriver.common.by import By


class HomePage(object):
    """ 主页模块模型 """

    def __init__(self):
        self.__to_loginpage = (By.CLASS_NAME, 'red')

    def loginpage_cls_name(self):
        """ 获取进入登录页元素 """
        return self.__to_loginpage
