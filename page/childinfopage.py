import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from base.base_action import BaseAction

#个人信息页
class ChildinfoPage(BaseAction):

    # 添加新成员按钮
    add_new_member = By.XPATH,'//*[@text="添加新成员"]'

    # 添加儿童信息页的的昵称
    nick_name = By.XPATH,'//*[@text="昵称"]'

    # 添加儿童信息页的的昵称-输入框
    nicknames_input = By.XPATH,'//android.widget.EditText'

    # 添加儿童信息页的弹框-确定按钮
    ok_button= By.XPATH,'//*[@text="确定"]'

    # 儿童信息页的信息-删除
    delect_button = By.XPATH, '//*[@text="删除"]'

    # 添加儿童信息页的完成对勾
    done_button = By.XPATH, '//*[@resource-id="fixedNav"]/android.widget.Image[2]'

    #昵称
    DADA = By.XPATH,'//*[@text="大大"]'
#昵称超过12个字提示文本
    message_1= By.XPATH,'//*[@text="最多可输入12个中文、英文或数字，请重新输入！"]'


    def click_add_new_member(self):
        self.click(self.add_new_member)


    def click_nick_name(self):
        self.click(self.nick_name)


    def input_nick_name(self,text):
        self.input(self.nicknames_input,text)

    def click_ok_button(self):
        self.click(self.ok_button)

    def click_done_button(self):
        self.click(self.done_button)

    def click_delect_button(self):
        self.click(self.delect_button)















