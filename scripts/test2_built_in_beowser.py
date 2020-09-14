#  内置浏览器  熊浩新增
import time
from base.driver import get_driver
from page.page import Page

class test_bewoser():

# InAppBrowser
    def setup(self):
        self.driver = get_driver()
        self.page = Page(self.driver)


    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    # 内置浏览器 熊浩 9-10
    def test_InAppBrowser_01(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“百度一下小爱同学”
        self.page.sessionpage.input_keyboard_input("百度一下小爱同学")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.is_toast_exist('小爱同学 - 百度')

    def test_InAppBrowser_02(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“狮子座的特点”
        self.page.sessionpage.input_keyboard_input("狮子座的特点")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 点击卡片icon
        self.page.sessionpage.click_small_card_icon()
        # 断言
        assert self.page.sessionpage.is_toast_exist('狮子座')

    def test_InAppBrowser_03(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“打开空气净化器”
        self.page.sessionpage.input_keyboard_input("打开空气净化器")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.is_toast_exist('支持小爱同学控制')