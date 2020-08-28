from selenium.webdriver.common.by import By


class AddressPage(object):
    """ 地址管理页 """

    def __init__(self):
        self.__add_address = (By.CLASS_NAME, 'co_blue')
        self.__address_count = (By.CSS_SELECTOR, '.gp_num2 em')

    def get_add_address_cls_name(self):
        return self.__add_address

    def get_address_count_css(self):
        return self.__address_count
