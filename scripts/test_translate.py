import time

from base.base_action import BaseAction
from base.driver import get_driver
from page.page import Page


class TestTranslate:
    def setup(self):
        self.driver = get_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()
#8.23新增（尚景）
    # 翻译小卡点击复制
    def test_copytext(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“警局的英文”
        self.page.sessionpage.input_keyboard_input("警局的英文")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        time.sleep(3)
        # 点击翻译小卡的复制按钮
        self.page.sessionpage.click_copy_btn()
        # 获取toast
        msg = self.page.sessionpage.ren_toast()
        # 断言
        assert "译文已经复制" in msg

    # 翻译小卡点击进入翻译页面
    def test_click_translation_btn(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“警局的英文”
        self.page.sessionpage.input_keyboard_input("警局的英文")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        time.sleep(3)
        # 点击小卡的对话翻译键
        self.page.sessionpage.click_translation_btn()
        # 断言
        ren_msg = self.page.sessionpage.ren_translation_title()
        assert "对话翻译" == ren_msg

