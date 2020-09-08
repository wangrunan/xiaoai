from selenium.common.exceptions import TimeoutException

from base.base_action import BaseAction
from selenium.webdriver.common.by import By

# 对话历史页
class HistoryRecordPage(BaseAction):

    # 发送的query
    send_query = By.XPATH, "//*[contains(@text,'今天天气')]"

    # 复制
    copy_button = By.XPATH,"//*[contains(@text,'复制')]"

    # 报错
    error_button = By.XPATH, "//*[contains(@text,'报错')]"

    # 举报
    inform_button = By.XPATH, "//*[contains(@text,'举报')]"

    # 标题
    tittle = By.ID,"com.xiaomi.xiaoailite:id/toolbar_title"

    def click_copy_button(self):
        self.click(self.copy_button)

    def click_error_button(self):
        self.click(self.error_button)

    def click_inform_button(self):
        self.click(self.inform_button)

    def long_press_query(self):
        self.long_press(self.send_query)

    def get_error_text(self):
        return self.get_text(self.error_button)

    def get_inform_text(self):
        return self.get_text(self.inform_button)

    def is_copy_exist(self):
        try:
            self.find_element6(self.copy_button)
            return True
        except TimeoutException:
            return False

    def is_error_exist(self):
        try:
            self.find_element6(self.error_button)
            return True
        except TimeoutException:
            return False

    def is_inform_exist(self):
        try:
            self.find_element6(self.inform_button)
            return True
        except TimeoutException:
            return False
