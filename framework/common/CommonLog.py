# -*- coding:utf-8 -*-

import time
import os
import logging
import sys
from functools import wraps
from framework import Var
from logging.handlers import RotatingFileHandler

logger = None


def retry(tries=1, delay=1, backoff=1, logger=None):
    def deco_retry(f):
        @wraps(f)   # 属性复制，相当于 f_retry.__name__ = f.__name__
        def f_retry(*args, **kwargs):
            mtries, mdelay = tries, delay
            while mtries > 1:
                result = result = f(*args, **kwargs)
                if result is None:
                    msg = "Retrying in " + str(mdelay) + " seconds..."
                else:
                    break

                if logger:
                    logger.warning(msg)
                else:
                    print (msg)
                time.sleep(mdelay)
                mtries -= 1
                mdelay *= backoff
            return result
        return f_retry
    return deco_retry


def init_logger(log_lever):
    # 初始化报告系统
    # if Var.ROOT:
    #     report_child = "{}_{}_{}".format(Var.project, Var.device_type, Var.report_time)
    #     Var.report_dir = os.path.join(Var.ROOT, "Report", report_child)
    #     if not os.path.exists(Var.report_dir):
    #         os.mkdir(Var.report_dir)
    Var.project = "AppiumAutoTest"    # 待优化为 自动获取当前运行工程名称
    Var.device_type = Var.platformName
    Var.report_time = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time()))  # 获取当前时间并格式化
    report_child = "{}_{}_{}".format(Var.project, Var.device_type, Var.report_time)
    Var.report_dir = os.path.join(Var.ROOT, "Report", report_child)
    if not os.path.exists(Var.report_dir):
        os.makedirs(Var.report_dir)

    log_file_name = os.path.join(Var.report_dir, "project.log")
    Var.project_log = os.path.join("http://*******", Var.report_dir.split(os.sep)[-1], "project.log")
    print ("Running log will be stored under {}").format(log_file_name)

    # get a root logger
    global logger
    logger = logging.getLogger()
    logger.setLevel(logging.NOTSET)

    # stream output to console
    ch = logging.StreamHandler(stream=sys.stdout)
    # stream output to log file
    rh = logging.handlers.RotatingFileHandler(log_file_name, mode="a", maxBytes=50 * 1024 * 1024, backupCount=10)

    # output format
    formatter = logging.Formatter('%(asctime)s %(levelname)s :%(message)s')
    ch.setFormatter(formatter)
    rh.setFormatter(formatter)
    ch.setLevel(log_lever)
    rh.setLevel(log_lever)

    # 给logger 添加handler
    logger.addHandler(ch)
    logger.addHandler(rh)

    logger.info("Logger is initialized")


def print_info(msg):
    try:
        logger.info(msg)
    except:
        print (msg)


def print_error(msg):
    try:
        logger.error(msg)
    except:
        print (msg)


def print_exec(e):
    try:
        logger.exception(e)
    except:
        print ("!!!!!!")



def Step(msg):
    # 日志同时输出到控制台和测试报告中Var.case_step_index += 1
    # Var.case_step_index = Var.case_step_index + 1
    Var.case_step_index += 1
    msg = "Step {}: ".format(str(Var.case_step_index)) + msg
    logger.info(msg)
    msg_new = time.strftime('%Y-%m-%d %H:%M:%S ', time.localtime(time.time())) + msg
    # Var.case_msg = Var.case_msg + "\n" + msg_new
