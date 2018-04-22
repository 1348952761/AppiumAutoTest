# -*- coding:utf-8 -*-
from framework import Var
from framework.common import CommonLog
import logging
from appium import webdriver
import time


def projectinit(caps):
    Var.case_step_index = 0
    Var.config_caps = caps
    CommonLog.init_logger(logging.NOTSET)
    Var.driver_instance = webdriver.Remote('http://127.0.0.1:4723/wd/hub', Var.config_caps)
    time.sleep(3)
