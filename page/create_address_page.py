from selenium.webdriver.common.by import By


class NewAddresspage(object):
    """ 新建地址页 """
    page_frame_tag = 'layui-layer-iframe100001'

    def __init__(self):
        self.__receiver = (By.CSS_SELECTOR, '.wi80-BFB')
        self.__province = (By.ID, 'province')
        self.__city = (By.ID, 'city')
        self.__district = (By.ID, 'district')
        self.__twon = (By.ID, 'twon')
        self.__address = (By.CSS_SELECTOR, '#address')
        self.__phone = (By.CSS_SELECTOR, '.wi40-BFB')
        self.__submit = (By.CSS_SELECTOR, '.ma-le--70')

    def get_receiver(self):
        return self.__receiver

    def get_province(self):
        return self.__province

    def get_city(self):
        return self.__city

    def get_district(self):
        return self.__district

    def get_twon(self):
        return self.__twon

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone

    def get_submit(self):
        return self.__submit
