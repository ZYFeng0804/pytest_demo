from selenium import webdriver

from selenium.webdriver.support.wait import WebDriverWait


class BaseDriver(object):
    """ driver对象基类 """
    driver = None

    def __init__(self, url):
        if self.driver is None:
            self.driver = webdriver.Chrome()
            self.driver.get(url)

    def get_current_url(self):
        """ 获取当前url """
        return self.driver.current_url

    def set_max_window(self):
        """ 全屏 """
        self.driver.maximize_window()
        pass

    def get_element(self, datas):
        """ 获取元素
         :return 元素对象
         """
        return self.driver.find_element(datas[0], datas[1])

    def quit(self):
        """ 退出driver对象 """
        self.driver.quit()

    def set_imp_wait(self, timeout):
        """ 设置全局元素等待 """
        self.driver.implicitly_wait(timeout)

    def set_sigle_wait(self, datas):
        """" 设置单一元素等待 """
        element = WebDriverWait(self.driver, 10, 1).until(lambda x: x.find_element(datas[0], datas[1]))
        return element

    def switch_window(self, handle):
        return self.driver.switch_to.window(handle)

    def get_current_window_handle(self):
        """ 获取当前窗口handle """
        return self.driver.current_window_handle

    def get_window_handles(self):
        """ 获取所有窗口handle """
        return self.driver.window_handles

    def switch_frame(self, frametag):
        """ 切换frame """
        self.driver.switch_to.frame(frametag)

    def scroll(self, start, end):
        """ 滑动 """
        js_move = "window.scrollTo({},{})".format(start, end)
        self.driver.execute_script(js_move)
