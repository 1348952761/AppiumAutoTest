# coding:utf-8
import time
import traceback
from framework.common.CommonLog import *
from framework import Var
from framework.devices.android.device_appium import AndroidDevice
from framework.devices.ios.device_appium import iOSDevice

try:
    if str(Var.platformName.lower()) == "android":
        device_instance = AndroidDevice
        Var.device_type = "android"
    elif str(Var.platformName.lower()) == "ios":
        device_instance = iOSDevice
        Var.device_type = "iOS"
    else:
        raise Exception("In config.py, platformName is not android or ios !")


except:
    # 默认设备为 android
    device_instance = AndroidDevice
    Var.device_type = "android"


class Device(object):

    @staticmethod
    def get_ui_object_by_id(resource_id="", single=True):
        '''
        点击指定id控件
        :param resource_id:
        :param check:
        :return:
        '''

        return device_instance.get_ui_object_by_id(resource_id, single)

    @staticmethod
    def click_accurate_x_y(view, ratio_x=0.5, ratio_y=0.5):
        width = view.size["width"]
        height = view.size["height"]
        if 0 <= ratio_x <= 1:
            x = int(view.location["x"] + width * ratio_x)
        elif ratio_x < 0:
            width = Var.driver_instance.get_window_size()["width"]
            x = int(view.location["x"] - width * (ratio_x * -1 - 1))
        else:
            width = Var.driver_instance.get_window_size()["width"]
            x = int(view.location["x"] + width * (ratio_x - 1))

        if 0 <= ratio_y <= 1:
            y = int(view.location["y"] + width * ratio_y)
        elif ratio_x < 0:
            width = Var.driver_instance.get_window_size()["height"]
            y = int(view.location["y"] - width * (ratio_y * -1 - 1))
        else:
            width = Var.driver_instance.get_window_size()["height"]
            y = int(view.location["y"] + width * (ratio_y - 1))
        Var.driver_instance.tap([(x, y), ])

    @staticmethod
    # @snapshot
    def click_by_id(resource_id="", check=True):
        '''
        点击指定id控件
        :param resource_id:
        :param check:
        :return:
        '''

        view = Device.get_ui_object_by_id(resource_id)
        if view:
            Device.click_accurate_x_y(view)
            time.sleep(1)
        else:
            if check:
                e = Exception("Can't find id:%s" % resource_id)
                print_error("           ！！！！！raise a exception！！！！！")
                print_exec(e)
                print_error("")
                raise e
