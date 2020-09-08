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

