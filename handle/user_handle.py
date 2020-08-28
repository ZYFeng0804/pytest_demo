from base.base_handle import BaseHandle
from page.user_page import UserPage


class UserHandle(BaseHandle):
    def __init__(self, driver):
        self.driver = driver
        self.userpage = UserPage()

    def to_orderpage(self):
        element = self.driver.set_sigle_wait(self.userpage.get_myorder())
        self.click_element(element)
