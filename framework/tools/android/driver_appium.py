# coding:utf-8
import time

from framework import Var
from appium import webdriver
from urllib2 import URLError
from selenium.common.exceptions import ErrorInResponseException
from selenium.common.exceptions import WebDriverException


def ProcessException(e):
    if isinstance(e,(AttributeError,URLError,ErrorInResponseException,WebDriverException)):
        # start_server(Var.sn)
        Var.driver_instance = webdriver.Remote('http://localhost:{}/wd/hub'.format(Var.device_port), Var.desired_caps)
        Var.AppiumDriver = Var.driver_instance
        return True
    return False

class AndroidDevice(object):
    @staticmethod
    # @retry
    def pinch():
        pass

    @staticmethod
    # @retry
    def zoom():
        pass

    @staticmethod
    # @retry
    def pinch():
        pass

    @staticmethod
    # @retry
    def swipe_to_begin(during=200):
        width = Var.driver_instance.get_window_size()['width'] / 2
        height = Var.driver_instance.get_window_size()['height'] /2
        Var.driver_instance.swipe(width / 2, height / 4, width / 2, height * 3 / 4, during)
        return True

    @staticmethod
    # @retry
    def swipe_to_end(during=200):
        width = Var.driver_instance.get_window_size()['width'] / 2
        height = Var.driver_instance.get_window_size()['height'] / 2
        Var.driver_instance.swipe(width / 2, height * 3 / 4, width / 2, height / 4, during)
        return True

    @staticmethod
    # @retry
    def swipe_to_right(during=200):
        width = Var.driver_instance.get_window_size()['width'] / 2
        height = Var.driver_instance.get_window_size()['height'] / 2
        Var.driver_instance.swipe(width * 6 / 7, height / 2, width / 7, height / 2, during)
        return True

    @staticmethod
    # @retry
    def swipe_to_left(during=200):
        width = Var.driver_instance.get_window_size()['width'] / 2
        height = Var.driver_instance.get_window_size()['height'] / 2
        Var.driver_instance.swipe(width / 7, height / 2, width * 6 / 7, height / 2, during)
        return True

    @staticmethod
    def input_text(element, text, clean):
        if clean:
            num = 0
            while True:
                context = element.get_attribute('name')  # 获取文本框内容，包括desc和text
                if num == len(context):
                    # 灰显的文本或无文本
                    break
                else:
                    num = len(context)
                    if len(context) > 0:
                        # 删除文本框中的内容
                        # KEYCODE_MOVE_END
                        Var.driver_instance.press_keycode(123)  # 光标移动到末尾
                        for i in range(0, len(context)):
                            Var.driver_instance.press_keycode(67)   # 按退格键
                    else:
                        break
        Var.driver_instance.set_value(element, text)
        return True

    @staticmethod
    def input_text_webview(element, text, clean, maxlen=10):
        if clean:
            # 删除文本框中的内容
            Var.driver_instance.press_keycode(123)  # 光标移动到末尾
            for i in range(0, maxlen):
                Var.driver_instance.press_keycode(67)   # 按退格键
        Var.driver_instance.set_value(element, text)

    @staticmethod
    def get_text(element):
        return element.get_attribute("name")

    @staticmethod
    # @retry
    def get_ui_object_by_text(text_str="", single=True):
        element = None
        try:
            element = Var.driver_instance.find_elements_by_android_uiautomator("new UiSelector().text(\"%s\")"%text_str)
        except Exception as e:
            if ProcessException(e):
                raise Exception("try again")
            return None
        if len(element) == 0:
            return None
        if single:
            return element[0]
        else:
            return element

    @staticmethod
    # @retry
    def get_ui_object_scroll_by_text(text_str="", step=100):
        width = Var.driver_instance.get_window_size()["width"]
        height = Var.driver_instance.get_window_size()["height"]
        # count = (int)(height / (step * 10))
        for i in range(5):
            element = None
            try:
                element = Var.driver_instance.find_elements_by_android_uiautomator("new UiSelector().text(\"%s\")"%text_str)
            except Exception as e:
                if i == 0:
                    AndroidDevice.swipe_to_begin()
                else:
                    Var.driver_instance.swipe(width / 2, height * 3 / 4, width / 2, height * 2 / 4, step * 10)
                time.sleep(0.5)
                continue
            return element

    @staticmethod
    # @retry
    def get_ui_object_by_text_contains(text_str="", single=True):
        element = None
        try:
            element = Var.driver_instance.find_elements_by_android_uiautomator("new UiSelector().textContains(\"%s\")"%text_str)
        except Exception as e:
            # if ProcessException(e):
            #     raise Exception("try again")
            return None
        if len(element) == 0:
            return None
        if single:
            return element[0]
        else:
            return element

    @staticmethod
    # @retry
    def get_ui_object_scroll_by_text_contains(text_str="", step=100):
        width = Var.driver_instance.get_window_size()["width"]
        height = Var.driver_instance.get_window_size()["height"]
        # count = (int)(height / (step * 10))
        for i in range(5):
            element = None
            try:
                element = Var.driver_instance.find_elements_by_android_uiautomator("new UiSelector().textContains(\"%s\")"%text_str)
            except Exception as e:
                if i == 0:
                    AndroidDevice.swipe_to_begin()
                else:
                    Var.driver_instance.swipe(width / 2, height * 3 / 4, width / 2, height * 2 / 4, step * 10)
                time.sleep(0.5)
                continue
            return element

    @staticmethod
    # @retry
    def get_ui_object_by_classname(classname="", single=True):
        element = None
        try:
            element = Var.driver_instance.find_elements_by_android_uiautomator(
                "new UiSelector().className(\"%s\")" % classname)
        except Exception as e:
            if ProcessException(e):
                raise Exception("try again")
            return None
        if len(element) == 0:
            return None
        if single:
            return element[0]
        else:
            return element

    @staticmethod
    # @retry
    def get_ui_object_by_id(id_str="", single=True):
        element = None
        try:
            element = Var.driver_instance.find_elements_by_android_uiautomator(
                "new UiSelector().resourceId(\"%s\")" % id_str)
            # element = Var.driver_instance.find_elements_by_android_uiautomator(
            #     r'''new UiSelector().resourceId("com.android.calculator2:id/digit_1")''')
        except Exception as e:
            if ProcessException(e):
                raise Exception("try again")
            return None
        if len(element) == 0:
            return None
        if single:
            return element[0]
        else:
            return element

    @staticmethod
    # @retry
    def get_ui_object_scroll_by_id(id_str="", step=100):
        width = Var.driver_instance.get_window_size()["width"]
        height = Var.driver_instance.get_window_size()["height"]
        # count = (int)(height / (step * 10))
        for i in range(5):
            element = None
            try:
                element = Var.driver_instance.find_elements_by_android_uiautomator(
                    "new UiSelector().resourceId(\"%s\")" % id_str)
            except Exception as e:
                if i == 0:
                    AndroidDevice.swipe_to_begin()
                else:
                    Var.driver_instance.swipe(width / 2, height * 3 / 4, width / 2, height * 2 / 4, step * 10)
                time.sleep(0.5)
                continue
            return element

    @staticmethod
    # @retry
    def get_ui_object_by_id_contains(id_str="", single=True):
        element = None
        try:
            element = Var.driver_instance.find_elements_by_android_uiautomator(
                "new UiSelector().resourceIdContains(\"%s\")" % id_str)
        except Exception as e:
            # if ProcessException(e):
            #     raise Exception("try again")
            return None
        if len(element) == 0:
            return None
        if single:
            return element[0]
        else:
            return element

    @staticmethod
    # @retry
    def get_ui_object_scroll_by_id_contains(id_str="", step=100):
        width = Var.driver_instance.get_window_size()["width"]
        height = Var.driver_instance.get_window_size()["height"]
        # count = (int)(height / (step * 10))
        for i in range(5):
            element = None
            try:
                element = Var.driver_instance.find_elements_by_android_uiautomator(
                    "new UiSelector().resourceIdContains(\"%s\")" % id_str)
            except Exception as e:
                if i == 0:
                    AndroidDevice.swipe_to_begin()
                else:
                    Var.driver_instance.swipe(width / 2, height * 3 / 4, width / 2, height * 2 / 4, step * 10)
                time.sleep(0.5)
                continue
            return element

    @staticmethod
    # @retry
    def get_ui_object_by_desc(desc_str="", single=True):
        element = None
        try:
            element = Var.driver_instance.find_elements_by_android_uiautomator(
                "new UiSelector().description(\"%s\")" % desc_str)
        except Exception as e:
            if ProcessException(e):
                raise Exception("try again")
            return None
        if len(element) == 0:
            return None
        if single:
            return element[0]
        else:
            return element

    @staticmethod
    # @retry
    def get_ui_object_scroll_by_desc(desc_str="", step=100):
        width = Var.driver_instance.get_window_size()["width"]
        height = Var.driver_instance.get_window_size()["height"]
        # count = (int)(height / (step * 10))
        for i in range(5):
            element = None
            try:
                element = Var.driver_instance.find_elements_by_android_uiautomator(
                    "new UiSelector().description(\"%s\")" % desc_str)
            except Exception as e:
                if i == 0:
                    AndroidDevice.swipe_to_begin()
                else:
                    Var.driver_instance.swipe(width / 2, height * 3 / 4, width / 2, height * 2 / 4, step * 10)
                time.sleep(0.5)
                continue
            return element

    @staticmethod
    # @retry
    def get_ui_object_by_desc_contains(desc_str="", single=True):
        element = None
        try:
            element = Var.driver_instance.find_elements_by_android_uiautomator(
                "new UiSelector().descriptionContains(\"%s\")" % desc_str)
        except Exception as e:
            # if ProcessException(e):
            #     raise Exception("try again")
            return None
        if len(element) == 0:
            return None
        if single:
            return element[0]
        else:
            return element

    @staticmethod
    # @retry
    def get_ui_object_scroll_by_desc_contains(desc_str="", step=100):
        width = Var.driver_instance.get_window_size()["width"]
        height = Var.driver_instance.get_window_size()["height"]
        # count = (int)(height / (step * 10))
        for i in range(5):
            element = None
            try:
                element = Var.driver_instance.find_elements_by_android_uiautomator(
                    "new UiSelector().descriptionContains(\"%s\")" % desc_str)
            except Exception as e:
                if i == 0:
                    AndroidDevice.swipe_to_begin()
                else:
                    Var.driver_instance.swipe(width / 2, height * 3 / 4, width / 2, height * 2 / 4, step * 10)
                time.sleep(0.5)
                continue
            return element

    @staticmethod
    # @retry
    def get_ui_object_by_xpath(xpath="", single=True):
        element = None
        try:
            element = Var.driver_instance.find_elements_by_xpath(xpath)
        except Exception as e:
            return None
        if len(element) == 0:
            return None
        if single:
            return element[0]
        else:
            return element

    @staticmethod
    # @retry
    def get_accurate_x_y(ui_object, ratio_x, ratio_y):
        length = ui_object.info["bounds"]["right"] - ui_object.info["bounds"]["left"]
        height = ui_object.info["bounds"]["bottom"] - ui_object.info["bounds"]["top"]
        x = ui_object.info["bounds"]["left"] + length * ratio_x
        x = ui_object.info["bounds"]["top"] + length * ratio_y
        return x, y
