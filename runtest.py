# coding:utf-8


import time
from appium import webdriver
from framework import *

print r"config文件中的配置 动态定义到 Var中"
Var.desired_caps = {
    "platformName": Var.platformName,
    "deviceName": Var.deviceName,
    "platformVersion": Var.platformVersion,
    # apk 包名
    "appPackage": Var.appPackage,
    # apk 的launcherActivity
    "appActivity": Var.appActivity,
    "device_port": Var.device_port
}
print u"创建 driver，并动态定义到 Var中"
Var.driver_instance = webdriver.Remote('http://127.0.0.1:4723/wd/hub', Var.desired_caps)
print u"创建 driver，并动态定义到 Var中 成功"
time.sleep(2)


try:

    Device.click_by_id("com.android.calculator2:id/digit_1")
    time.sleep(3)
    Device.click_by_id("com.android.calculator2:id/op_add")
    time.sleep(3)
    Device.click_by_id("com.android.calculator2:id/digit_2")
    time.sleep(3)
    Device.click_by_id("com.android.calculator2:id/eq")
finally:
    Var.driver_instance.quit()   # 避免appium报错 Failed to start an Appium session, err was: Error: Requested a new session but one was in progress
