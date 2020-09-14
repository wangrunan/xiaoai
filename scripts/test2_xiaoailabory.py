import time

from base.base_action import BaseAction
from base.driver import get_driver
from page.page import Page


class Testxiaoailabory:
    def setup(self):
        self.driver = get_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()
#8.29何巧
# 小爱实验室里点击音色设置
    def test_click_Voicesettings_tab(self):
        self.page.homepage.click_center_button()
        # 点击"小爱实验室"
        self.page.centerpage.click_xiaoai_lab()
        #点击音色设置tab
        self.page.xiaoailaboratorypage.click_Voicesettings_tap()
        #断言-页面跳转正常
        assert self.driver.current_activity == ".presenter.activity.ToneSettingActivity"
# 小爱实验室里点击小爱悬浮球
    def test_click_Littlelovefloatingball_tab(self):
        self.page.homepage.click_center_button()
        # 点击"小爱实验室"
        self.page.centerpage.click_xiaoai_lab()
        #点击音色设置tab
        self.page.xiaoailaboratorypage.click_Littlelovefloatingball_tap()
        #断言-页面跳转正常
        assert self.driver.current_activity == ".presenter.activity.SettingFloatBallActivity"

    # 何巧新增  9.11
        # 9.12何巧
        # 点击小爱悬浮球页面-选择唤醒方式-长按唤醒
    def test_click_Littlelovefloatingball01_longpress_workup(self):
        self.page.homepage.click_center_button()
        # 点击"小爱实验室"
        self.page.centerpage.click_xiaoai_lab()
        # 点击音色设置tab
        self.page.xiaoailaboratorypage.click_Littlelovefloatingball_tap()
        # 点击唤醒方式
        self.page.littlefloationballPage.click_Wakeupmode_button()
        # 点击长按唤醒
        self.page.littlefloationballPage.click_longpress_Wakeupmode_button()
        # 断言-唤醒方式后面的文本是：长按唤醒
        assert self.page.littlefloationballPage.get_text(
            self.page.littlefloationballPage.workupmethond_button) == "长按唤醒"

        # 点击小爱悬浮球页面-选择唤醒方式-长按唤醒
    def test_click_Littlelovefloatingball02_double_workup(self):
        self.page.homepage.click_center_button()
        # 点击"小爱实验室"
        self.page.centerpage.click_xiaoai_lab()
        # 点击音色设置tab
        self.page.xiaoailaboratorypage.click_Littlelovefloatingball_tap()
        # 点击唤醒方式
        self.page.littlefloationballPage.click_Wakeupmode_button()
        # 点击长按唤醒
        self.page.littlefloationballPage.click_double_Wakeupmode_button()
        # 断言-唤醒方式后面的文本是：长按唤醒
        assert self.page.littlefloationballPage.get_text(
            self.page.littlefloationballPage.workupmethond_button) == "双击唤醒"

        # 点击小爱悬浮球页面-选择唤醒方式-单击唤醒
    def test_click_Littlelovefloatingball03_single_workup(self):
        self.page.homepage.click_center_button()
        # 点击"小爱实验室"
        self.page.centerpage.click_xiaoai_lab()
        # 点击音色设置tab
        self.page.xiaoailaboratorypage.click_Littlelovefloatingball_tap()
        # 点击唤醒方式
        self.page.littlefloationballPage.click_Wakeupmode_button()
        # 点击单击唤醒
        self.page.littlefloationballPage.click_single_Wakeupmode_button()
        # 断言-唤醒方式后面的文本是：单击唤醒
        assert self.page.littlefloationballPage.get_text(
            self.page.littlefloationballPage.workupmethond_button) == "单击唤醒"



