import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def find_element6(self, tuple, timeout=15 ,poll=1.0):
        by = tuple[0]
        value = tuple[1]
        return WebDriverWait(self.driver, timeout, poll).until(lambda x:x.find_element(by, value))

    # 查找多元素方法
    def find_elements(self, feature, timeout=10, poll=1.0):
        by = feature[0]
        value = feature[1]

        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(by, value))

    def click(self, feature):
        self.find_element6(feature).click()

    def input(self, feature, text):
        self.find_element6(feature).send_keys(text)
    # 清空方法
    def clear_test(self,feature):
        self.find_element6(feature).clear()

    def get_text(self, feature):
        return self.find_element6(feature).text

    def get_text_scroll(self, feature):
        return self.find_element_with_scroll(feature).text

    def is_button_exist(self,feather):

        try:
            self.find_element6(feather)
            return False
        except Exception:
            return True

    def is_toast_exist(self, message):
        """
        根据 部分内容，判断toast是否存在
        :param message: 部分内容
        :return: 是否存在
        """
        message_xpath = By.XPATH, "//*[contains(@text,'%s')]" % message
        try:
            self.find_element6(message_xpath, 5, 0.1)
            return True
        except TimeoutException:
            return False

    def get_toast_text(self, message):
        """
        根据 部分内容，获取toast上的所有内容
        :param message: 部分内容
        :return: 所有内容
        """
        if self.is_toast_exist(message):
            message_xpath = By.XPATH, "//*[contains(@text,'%s')]" % message
            return self.find_element6(message_xpath, 5, 0.1).text
        else:
            raise Exception("toast未出现，请检查参数是否正确或toast有没有出现在屏幕上")

    def scroll_page_one_time(self, direction="up"):

        height = self.driver.get_window_size()["height"]
        width = self.driver.get_window_size()["width"]

        left_x = width / 4
        lefy_y = height / 2
        right_x = width / 4 * 3
        right_y = height / 2

        top_x = width / 2
        top_y = height / 4 * 1
        bottom_x = width / 2
        bottom_y = height / 4 * 3

        if direction == "up":
            self.driver.swipe(bottom_x, bottom_y, top_x, top_y, 3000)
        elif direction == "down":
            self.driver.swipe(top_x, top_y, bottom_x, bottom_y, 3000)
        elif direction == "right":
            self.driver.swipe(left_x, lefy_y, right_x, right_y, 3000)
        elif direction == "left":
            self.driver.swipe(right_x, right_y, left_x, lefy_y, 3000)
        else:
            raise Exception("请检查参数")

    def find_element_with_scroll(self, featrue, diretion="up"):
        page_source = ""
        while True:
            try:
                return self.find_element6(featrue)
            except Exception:
                self.scroll_page_one_time(diretion)
                if self.driver.page_source == page_source:
                    print("到底了")
                    break
                page_source = self.driver.page_source

    # 长按
    def long_press(self,message):
        action = TouchAction(self.driver)
        element = self.find_element6(message, 5, 0.1)
        action.press(el=element).wait(3000).release().perform()








