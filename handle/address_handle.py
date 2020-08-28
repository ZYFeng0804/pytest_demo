from base.base_handle import BaseHandle
from page.address_page import AddressPage


class AddressHandle(BaseHandle):
    """ 地址操作类 """

    def __init__(self, driver):
        self.driver = driver
        self.addresspage = AddressPage()

    def get_address_count(self):
        element = self.driver.get_element(self.addresspage.get_address_count_css())
        return self.get_text_2_int(element)

    def to_add_address_frame(self):
        element = self.driver.get_element(self.addresspage.get_add_address_cls_name())
        self.click_element(element)
