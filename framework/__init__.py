# -*- coding:utf-8 -*-
import inspect
import os
VERSION = "1.0.0"


from framework.common.Variable import Variable

Var = Variable()

from framework.devices.device_appium import Device


print("AppiumAutoTest version is %s" % VERSION)
if not Var.ROOT:
    for path in inspect.stack():
        if str(path[1]).endswith("runtest.py") or str(path[1]).endswith("runtest_android.py"):
            Var.ROOT = os.path.dirname(path[1])
            if "framework" in Var.ROOT:
                Var.ROOT = None
            break

from framework.utils.projectutils import *
from framework.common.CommonLog import *