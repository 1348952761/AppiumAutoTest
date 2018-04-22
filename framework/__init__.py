# -*- coding:utf-8 -*-

VERSION = "1.0.0"


from framework.common.Variable import Variable

Var = Variable()

from framework.tools.devices.driver_appium import Device


print("AppiumAutoTest version is %s" % VERSION)
