from selenium.webdriver.common.by import By


class UserPage(object):
    """" 个人中心 """

    def __init__(self):
        self.__my_order = (By.CSS_SELECTOR, '.top-ri-header a')
        pass

    def get_myorder(self):
        return self.__my_order
