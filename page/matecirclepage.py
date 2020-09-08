from selenium.webdriver.common.by import By
from time import sleep
from base.base_action import BaseAction

# 登录页
class MateCirclePage(BaseAction):

    #关注按钮
    follow_button = By.XPATH, "//*[@text='关注']"

    #默认昵称
    Defaultnickname=By.XPATH, "//*[@text='默认昵称']"
    #已关注按钮
    Nofollow_button = By.XPATH, "//*[@text='已关注']"

    def click_follow_button(self):
        self.find_element_with_scroll(self.follow_button).click()

    def click_Defaultnickname_button(self):
        self.find_element_with_scroll(self.Defaultnickname).click()

    def click_Nofollow_button(self):
        self.find_element_with_scroll(self.Nofollow_button).click()
