# coding:utf-8

import time
from appium import webdriver

desired_capabilities = {
    'platformName': 'Android',
    'deviceName': '192.168.22.101:5555',
    'platformVersion': '6.0',
    # apk 包名
    'appPackage': 'com.android.calculator2',
    # apk 的launcherActivity
    'appActivity': '.Calculator'
}
# 127.0.0.1:4723是 Appium 服务的地址和端口
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities)
time.sleep(10)
try:
    driver.find_element_by_id("com.android.calculator2:id/digit_1").click()
    time.sleep(3)
    driver.find_element_by_id("com.android.calculator2:id/op_add").click()
    time.sleep(3)
    driver.find_element_by_id("com.android.calculator2:id/digit_2").click()
    time.sleep(3)
    driver.find_element_by_id("com.android.calculator2:id/eq").click()
    print driver.find_element_by_id("com.android.calculator2:id/formula").get_attribute("text")
finally:
    driver.quit()   # 避免appium报错 Failed to start an Appium session, err was: Error: Requested a new session but one was in progress
