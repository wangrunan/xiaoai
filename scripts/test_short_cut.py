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





# #快捷方式页-点击添加-有弹窗-点击添加-点击确定-点击添加
#     #没有弹窗-点击添加
#     def test_school_timetable_add(self):
#         # step1 首页点击个人中心按钮
#         time.sleep(3)
#         self.page.homepage.click_center_button()
#         print("1")
#
#         # 调用croll_page_one_time()方法 滑动屏幕
#         self.page.shortcutpage.scroll_page_one_time()
#         print("2")
#
#
#
#         #step2 点击个人中心页面“快捷方式”
#         self.page.centerpage.click_shortcut_tab()
#
#         time.sleep(2)
#         print("3")
#         #step4 点击快捷方式页面--课程表——添加
#
#         self.page.shortcutpage.click_school_timetable_add()
#         print("4")
#         time.sleep(2)
#         #  判断是否有添加到桌面的弹窗
#         if self.page.shortcutpage.if_exist_pop_up_window:
#             # step6 有添加到桌面的弹窗就点击添加
#             self.page.shortcutpage.click_school_home_screen_add()
#             print("5")
#             time.sleep(1)
#             # 点击确定
#             #self.page.shortcutpage.click_add_to_the_desktop_confirm()
#             print("6")
#
#             #  点击快捷方式页面--课程表——添加
#             self.page.shortcutpage.click_school_timetable_add()
#             print("7")
#
#             #  断言是否创建成功
#             assert self.page.shortcutpage.is_toast_exist("已创建")
#             return
#
#         # # 没出现弹窗，直接断言是否创建成功
#         #      #点击返回
#         # self.page.shortcutpage.click_back_button()
#         # # step2 点击个人中心页面“快捷方式”
#         # self.page.centerpage.click_shortcut_tab()
#         # self.page.shortcutpage.click_school_timetable_add()
#
#         assert self.page.shortcutpage.is_toast_exist("已创建")



        # 快捷方式-添加课程表
        def test_school_timetable_add(self):
            # step1 首页点击个人中心按钮
            time.sleep(3)
            self.page.homepage.click_center_button()

            # step2 点击个人中心页面“快捷方式”
            self.page.centerpage.click_shortcut_tab()

            # # step3 断言是否跳转到“快捷方式”页面
            # assert self.page.stortcutpage.get_text(self.page.stortcutpage.stort_cut_title)=='快捷方式'

            time.sleep(2)
            # step4 点击快捷方式页面--课程表——添加

            self.page.shortcutpage.click_school_timetable_add()

            # step5 判断是否有添加到桌面的弹窗
            if self.driver.find_elements_by_xpath("//*[contains(@resource-id,'widget_name')]"):

                # step6 有添加到桌面的弹窗就点击添加
                self.page.shortcutpage.click_school_home_screen_add()
                time.sleep(1)

                # step7 判断是否有已尝试添加到桌面的弹窗
                if self.driver.find_elements_by_id("com.xiaomi.xiaoailite:id/btn_confirm"):
                    # if self.page.shortcutpage.is_button_exist(self.page.shortcutpage.is_add_desk_allary_exist):
                    # if self.page.shortcutpage.is_add_desk_allary_exist():

                    # step8 判断是否有已尝试添加到桌面的弹窗，有就点击确定
                    self.page.shortcutpage.click_add_to_the_desktop_confirm()

                # step8 点击快捷方式页面--课程表——添加
                self.page.shortcutpage.click_school_timetable_add()

                # step9 断言是否创建成功
                assert self.page.shortcutpage.is_toast_exist("该应用桌面快捷方式已创建")


            # step10 没出现弹窗，直接断言是否创建成功
            else:
                assert self.page.shortcutpage.is_toast_exist("该应用桌面快捷方式已创建")






    def test_xiaoai_translate_add(self):
        # step1 首页点击个人中心按钮
        time.sleep(3)
        self.page.homepage.click_center_button()


        # 调用croll_page_one_time()方法 滑动屏幕
        self.page.shortcutpage.scroll_page_one_time()


        #step2 点击个人中心页面“快捷方式”
        self.page.centerpage.click_shortcut_tab()


        time.sleep(2)
        #step4 点击快捷方式页面--课程表——添加

        self.page.shortcutpage.click_xiaoai_translate_add()
        time.sleep(2)
        print("4")
        #  判断是否有添加到桌面的弹窗
        if self.driver.find_elements_by_xpath("//*[contains(@resource-id,'widget_name')]"):
            # step6 有添加到桌面的弹窗就点击添加
            self.page.shortcutpage.click_xiaoai_translate_button()
            time.sleep(1)
            # 判断是否有已尝试添加到桌面的弹窗
            if self.driver.find_elements_by_id("com.xiaomi.xiaoailite:id/btn_confirm"):
                #判断是否有已尝试添加到桌面的弹窗，有就点击确定
                self.page.shortcutpage.click_add_to_the_desktop_confirm()



            #  点击快捷方式页面--课程表——添加
            self.page.shortcutpage.click_xiaoai_translate_add()
            print("7")

            #  断言是否创建成功
            assert self.page.shortcutpage.is_toast_exist("已创建")
            #return

        # # 没出现弹窗，直接断言是否创建成功
        #      #点击返回
        # self.page.shortcutpage.click_back_button()
        # # step2 点击个人中心页面“快捷方式”
        # self.page.centerpage.click_shortcut_tab()
        # self.page.shortcutpage.click_school_timetable_add()
        assert self.page.shortcutpage.is_toast_exist("已创建")



