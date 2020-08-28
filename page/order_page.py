from selenium.webdriver.common.by import By


class OrderPage(object):
    """ 订单页 """

    def __init__(self):
        self.__search_bt = (By.CLASS_NAME, '.sea_et')
        self.__address_mg = (By.LINK_TEXT, '地址管理')

    def get_searchbt_cls_name(self):
        return self.__search_bt

    def get_addressmg_link(self):
        return self.__address_mg
