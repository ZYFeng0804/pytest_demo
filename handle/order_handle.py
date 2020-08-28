from base.base_handle import BaseHandle
from page.order_page import OrderPage


class OrderHandle(BaseHandle):
    def __init__(self, driver):
        self.driver = driver
        self.orderpage = OrderPage()

    def page_is_loaded(self):
        """ 用页面独有元素确认页面加载完毕 """
        self.driver.set_sigle_wait(self.orderpage.get_searchbt_cls_name())

    def to_addresspage(self):
        """ 进入地址管理页 """
        element = self.driver.get_element(self.orderpage.get_addressmg_link())
        self.click_element(element)
