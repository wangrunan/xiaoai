import time

from base.base_action import BaseAction
from base.driver import get_driver
from page.page import Page


class TestShortCut:
    def setup(self):
        self.driver = get_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()


# 9.6 王茹楠

    #点击个人中心——快捷方式页面-点击返回-个人中心页
    def test_back_button(self):

        #step1 首页点击个人中心按钮
        self.page.homepage.click_center_button()

        #step2 点击个人中心页面“快捷方式”
        self.page.centerpage.click_shortcut_tab()

        #step3 断言是否跳转到“快捷方式”页面
        assert self.page.shortcutpage.get_text(self.page.shortcutpage.stort_cut_title)=="快捷方式"

        #step4 点击返回
        self.page.shortcutpage.click_back_button()

        # step5 断言是否成功
        assert self.page.centerpage.get_text(self.page.centerpage.tittle)=="个人中心"





#快捷方式页-点击添加-有弹窗-点击添加-点击确定-点击添加
    #没有弹窗-点击添加
    def test_school_timetable_add(self):
        # step1 首页点击个人中心按钮
        time.sleep(3)
        self.page.homepage.click_center_button()

        #step2 点击个人中心页面“快捷方式”
        self.page.centerpage.click_shortcut_tab()

        time.sleep(2)
        #step4 点击快捷方式页面--课程表——添加

        self.page.shortcutpage.click_school_timetable_add()
        time.sleep(2)
        #  判断是否有添加到桌面的弹窗
        if self.page.shortcutpage.if_exist_pop_up_window:
            # step6 有添加到桌面的弹窗就点击添加
            self.page.shortcutpage.click_school_home_screen_add()
            time.sleep(1)
            # 点击确定
            self.page.shortcutpage.click_add_to_the_desktop_confirm()

            #  点击快捷方式页面--课程表——添加
            self.page.shortcutpage.click_school_timetable_add()

            #  断言是否创建成功
            assert self.page.shortcutpage.is_toast_exist("已创建")
            return

        # # 没出现弹窗，直接断言是否创建成功
        #      #点击返回
        # self.page.shortcutpage.click_back_button()
        # # step2 点击个人中心页面“快捷方式”
        # self.page.centerpage.click_shortcut_tab()
        # self.page.shortcutpage.click_school_timetable_add()
        assert self.page.shortcutpage.is_toast_exist("已创建")



