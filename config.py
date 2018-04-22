# -*- coding:utf-8 -*-

project_config = {

    "platformName": "Android",
    "deviceName": "192.168.22.101:5555",
    "platformVersion": "6.0",
    # apk 包名
    "appPackage": "com.android.calculator2",
    # apk 的launcherActivity
    "appActivity": ".Calculator",
    "device_port": "4723"



    # "project": "sshd",
    # "platform": "Android",
    # "testType": "RegressionTest",
    # "scripts": "TC030201-26.xml",
    # "testTarget": "",
    # "owner": "imobiletest",
    # "sn": "e3c76a5c",
    # "env": "DevEnv",
    # "imobilecashier": "10.209.152.25",
    # "monitor": False,
    # "remotereport": False,
    # "remoteport": 8888,
    # "covercase": False,
    # "remoteAdbHost": '10.63.73.82',
    # "remoteAdbPort": "5037",
    # "adb_cmd": "adb",
    # # "server_ip": "11.166.12.65"
}

global_data = {
    # 工程全局的参数
    # 去除异常弹框
    "unexpect_element": {
        "name": [u"允许"],
        "id": ["com.android.packageinstaller:id/permission_allow_button"],
        "xpath": [],
        "classname": [],
        "css": []
    },
    "account": {
        "loginId1": "18924215680",  # "kyc未认证, 有交易记录和充值记录"
        "loginId2": "18964397455",  # 未绑卡用户
        "loginId4": "15881753106",  # "未激活账户"
        "loginId6": "hkbuyer_1967@alitest.com",  # "未激活账户"
    },
    "server_ip": "11.166.21.144"
}

