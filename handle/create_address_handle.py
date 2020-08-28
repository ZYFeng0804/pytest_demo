from base.base_handle import BaseHandle
from page.create_address_page import NewAddresspage


class CreatAddressHandle(BaseHandle):
    """ 新建地址handle类 """

    def __init__(self, driver):
        self.driver = driver
        self.newAddressPage = NewAddresspage()

    def input_receiver(self, text):
        element = self.driver.set_sigle_wait(self.newAddressPage.get_receiver())
        self.input_text(element, text)

    def input_province(self, text):
        element = self.driver.set_sigle_wait(self.newAddressPage.get_province())
        self.select_by_visible_text(element, text)

    def input_city(self, text):
        element = self.driver.set_sigle_wait(self.newAddressPage.get_city())
        self.select_by_visible_text(element, text)

    def input_district(self, text):
        element = self.driver.set_sigle_wait(self.newAddressPage.get_district())
        self.select_by_visible_text(element, text)

    def input_twon(self, text):
        element = self.driver.set_sigle_wait(self.newAddressPage.get_twon())
        self.select_by_visible_text(element, text)

    def input_address(self, text):
        element = self.driver.set_sigle_wait(self.newAddressPage.get_address())
        self.input_text(element, text)

    def input_phone(self, text):
        element = self.driver.set_sigle_wait(self.newAddressPage.get_phone())
        self.input_text(element, text)

    def click_submit(self):
        element = self.driver.set_sigle_wait(self.newAddressPage.get_submit())
        self.click_element(element)
