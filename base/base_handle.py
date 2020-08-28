from selenium.webdriver.support.select import Select


class BaseHandle(object):
    """ 元素操作基类 """

    def input_text(self, element, text):
        """ 输入文本 """
        try:
            element.clear()
            element.send_keys(text)
        except Exception as e:
            print('输入内容：', e)
            raise

    def click_element(self, element):
        """ 元素点击 """
        try:
            element.click()
        except Exception as e:
            print('点击元素：', e)
            raise

    def get_text(self, element):
        """ 获取元素文本 """
        try:
            return element.text
        except Exception as e:
            print('获取元素文本：', e)
            raise

    def get_text_2_int(self, element):
        """ 获取元素文本并转为int类型 """
        try:
            return int(element.text)
        except Exception as e:
            print('获取元素文本(int类型)：', e)
            raise

    def select_by_visible_text(self, element, text):
        """ 通过内容文本，选择下拉框项 """
        Select(element).select_by_visible_text(text)
