import time
import allure
import pytest

from base.base_driver import BaseDriver
from handle.address_handle import AddressHandle
from handle.create_address_handle import CreatAddressHandle
from handle.user_handle import UserHandle
from handle.home_handle import HomeHandle
from handle.login_handle import LoginHandle
from handle.order_handle import OrderHandle
from page.create_address_page import NewAddresspage


@allure.feature("添加收货地址流程")
class TestLogin:
    driver = None

    def setup_class(self):
        self.driver = BaseDriver('http://localhost/')
        self.driver.set_max_window()
        self.driver.set_imp_wait(10)

    def teardown_class(self):
        time.sleep(2)
        self.driver.quit()
        pass

    @allure.title("主页")
    @allure.description("用例描述：从主页跳转至登录页")
    @pytest.mark.run(order=1)
    def test_to_loginpage(self):
        homehandle = HomeHandle(self.driver)
        homehandle.go_2_loginpage()

    @allure.title("登录页")
    @allure.description("用例描述：成功登录")
    @pytest.mark.parametrize(("username", "password", "veriycode"),
                             [("18588581997", "123456", "8888")])
    @pytest.mark.run(order=2)
    def test_login(self, username, password, veriycode):
        loginhandle = LoginHandle(self.driver)
        loginhandle.input_username(username)
        loginhandle.input_password(password)
        loginhandle.input_veriycode(veriycode)
        loginhandle.click_login()

    @allure.title("我的订单页")
    @allure.description("用例描述：进入我的订单页")
    @pytest.mark.run(order=3)
    def test_to_myorderpage(self):
        userhandle = UserHandle(self.driver)
        userhandle.to_orderpage()

    # @pytest.mark.skip
    @allure.title("地址管理页")
    @allure.description("用例描述：地址管理页进入添加界面")
    @pytest.mark.run(order=4)
    def test_to_addresspage(self):
        # 切换窗口
        time.sleep(5)
        windows = self.driver.get_window_handles()
        self.driver.switch_window(windows[-1])
        orderhandle = OrderHandle(self.driver)
        self.driver.scroll(0, 200)
        orderhandle.to_addresspage()

    old_address_count = None

    # @pytest.mark.skip
    @allure.title("添加地址页")
    @allure.description("用例描述：进行添加地址操作，并验证结果")
    @pytest.mark.run(order=5)
    @pytest.mark.parametrize(("receiver", "province", "city", "district", "twon", "address", "phone"),
                             [("张先生", "北京市", "市辖区", "朝阳区", "三里屯街道", "xxx小区x单元xxx号", "15888888888")])
    def test_add_address(self, receiver, province, city, district, twon, address, phone):
        addresshandle = AddressHandle(self.driver)
        self.old_address_count = addresshandle.get_address_count()
        addresshandle.to_add_address_frame()
        time.sleep(2)
        # 切换frame
        self.driver.switch_frame(NewAddresspage.page_frame_tag)
        creataddresshandle = CreatAddressHandle(self.driver)
        # 写入数据
        creataddresshandle.input_receiver(receiver)
        creataddresshandle.input_province(province)
        creataddresshandle.input_city(city)
        creataddresshandle.input_district(district)
        creataddresshandle.input_twon(twon)
        creataddresshandle.input_address(address)
        creataddresshandle.input_phone(phone)
        creataddresshandle.click_submit()

        time.sleep(2)
        now_address_count = addresshandle.get_address_count()
        assert now_address_count > self.old_address_count, '最新地址条数是否大于之前，如成立则表示添加地址成功'
