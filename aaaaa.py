import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import TimeoutException

# desired_caps = dict()
# desired_caps['platformName'] = 'Android'
# desired_caps['platformVersion'] = '9'
# desired_caps['deviceName'] = '192.168.56.101:5555'
# desired_caps['appPackage'] = 'com.xiaomi.xiaoailite'
# desired_caps['appActivity'] = '.presenter.main.MainTabActivity'
# # toast
# desired_caps['automationName'] = 'Uiautomator2'
# # 是否重置应用 True:不重置 False:重置
# desired_caps['noReset'] = True
# driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# driver.implicitly_wait(3)
# driver.find_element_by_xpath("//*[@resource-id='com.xiaomi.xiaoailite:id/iv_login']").click()
# driver.find_element_by_id("com.xiaomi.xiaoailite:id/tv_history_record").click()
# time.sleep(5)
# action = TouchAction(driver)
# element = driver.find_element_by_xpath("//*[contains(@text,'今天天气')]")
# action.long_press(el=element, duration=3000).perform()
# time.sleep(3)
# print(driver.current_activity)
# print(driver.contexts)
# print(driver.page_source)
# driver.find_element_by_xpath( "//*[@text='报错']").click()

# driver.find_element_by_xpath("//*[@resource-id='com.xiaomi.xiaoailite:id/iv_login']").click()
# time.sleep(3)
# driver.press_keycode(4)
# time.sleep(3)
# driver.find_element_by_xpath("//*[@resource-id='com.xiaomi.xiaoailite:id/iv_login']").click()
# driver.find_element_by_id("com.xiaomi.xiaoailite:id/iv_clear_cache_arrow").click()
# def is_toast_exist(message):
#     """
#     根据 部分内容，判断toast是否存在
#     :param message: 部分内容
#     :return: 是否存在
#     """
#     try:
#         driver.find_element_by_xpath("//*[contains(@text,'%s')]" % message)
#         return True
#     except TimeoutException:
#         return False
# print(is_toast_exist('没有什么可清理'))


# print(driver.find_element_by_xpath("//*[contains(@text,'没有什么可清理')]").text)


# a = driver.find_element_by_id("com.xiaomi.xiaoailite:id/tv_shortcut")
# b = driver.find_element_by_id("com.xiaomi.xiaoailite:id/v_user_account")
# driver.drag_and_drop(origin_el = a,destination_el = b)
# action = TouchAction(driver)
# action.tap(x=970,y=1756).perform()
# action.release()
# time.sleep(5)


# driver.quit()

ts = time.time()
print(ts)
print(type(ts))
a= str(ts)
print(a)
print(type(a))