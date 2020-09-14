# 何巧新增  小爱悬浮球
from base.base_action import BaseAction
from selenium.webdriver.common.by import By
#9.12 何巧
# 小爱悬浮球页面
class LittlefloationballPage(BaseAction):
    #唤醒方式的按钮
    Wakeupmode_button = By.XPATH, "//*[contains(@text,'唤醒方式')]"
    #长按唤醒，双击唤醒，单击唤醒
    # longpress_Wakeupmode_button = By.XPATH, "//*[contains(@text,'长按唤醒')]"
    Wakeupmode_method_button =  By.ID,"com.xiaomi.xiaoailite:id/text"
    #唤醒方式后面的方式
    workupmethond_button = By.ID,"com.xiaomi.xiaoailite:id/tv_current_setting"
    #xpath://*[@resource-id="com.xiaomi.xiaoailite:id/tv_current_setting"]

#点击唤醒方式的按钮
    def click_Wakeupmode_button(self):
        self.click(self.Wakeupmode_button)
#点击长按唤醒的按钮
    def click_longpress_Wakeupmode_button(self):
        ele = self.find_elements(self.Wakeupmode_method_button)
        ele[0].click()
    # def click_longpress_Wakeupmode_button(self,text):
    #     self.click(self.longpress_Wakeupmode_button)
#点击双击唤醒的按钮
    def click_double_Wakeupmode_button(self):
        ele = self.find_elements(self.Wakeupmode_method_button)
        ele[1].click()

#点击单击唤醒的按钮
    def click_single_Wakeupmode_button(self):
        ele = self.find_elements(self.Wakeupmode_method_button)
        ele[2].click()