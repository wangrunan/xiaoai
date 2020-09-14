import time

from base.base_action import BaseAction
from base.driver import get_driver
from page.page import Page


class TestLikeDislike:
    def setup(self):
        self.driver = get_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    # 小卡点赞
    def test_click_like_dislike01(self):
        time.sleep(2)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“今天天气”
        self.page.sessionpage.input_keyboard_input("今天天气")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.like_dislike_text) == "本次回答满意吗？"
        # 点击点赞按钮
        self.page.sessionpage.click_like_button()
        time.sleep(2)
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.like_text) == "开心，我会再接再厉加油的！"

    # 小卡点踩
    def test_click_like_dislike02(self):
        time.sleep(2)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“今天天气”
        self.page.sessionpage.input_keyboard_input("今天天气")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.like_dislike_text) == "本次回答满意吗？"
        # 点击点赞按钮
        self.page.sessionpage.click_dislike_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.dislike_text) == "哎呀，抱歉，我会再努力的~"

    # 大卡点赞
    def test_click_like_dislike03(self):
        time.sleep(2)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“古诗词”
        self.page.sessionpage.input_keyboard_input("古诗词")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.like_dislike_text) == "本次回答满意吗？"
        # 点击点赞按钮
        self.page.sessionpage.click_like_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.like_text) == "开心，我会再接再厉加油的！"

    # 大卡点踩
    def test_click_like_dislike04(self):
        time.sleep(2)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“古诗词”
        self.page.sessionpage.input_keyboard_input("古诗词")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.like_dislike_text) == "本次回答满意吗？"
        # 点击点赞按钮
        self.page.sessionpage.click_dislike_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.dislike_text) == "哎呀，抱歉，我会再努力的~"

    # tts回复点赞
    def test_click_like_dislike05(self):
        time.sleep(2)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“你好”
        self.page.sessionpage.input_keyboard_input("你好")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.like_dislike_text) == "本次回答满意吗？"
        # 点击点赞按钮
        self.page.sessionpage.click_like_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.like_text) == "开心，我会再接再厉加油的！"

    # tts回复点踩
    def test_click_like_dislike06(self):
        time.sleep(2)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“你好”
        self.page.sessionpage.input_keyboard_input("你好")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.like_dislike_text) == "本次回答满意吗？"
        # 点击点赞按钮
        self.page.sessionpage.click_dislike_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.dislike_text) == "哎呀，抱歉，我会再努力的~"

# 8.23新增（刘锐）
    #跳转第三方应用，无点赞点踩
    def test_click_like_dislike07(self):
        time.sleep(2)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“你好”
        self.page.sessionpage.input_keyboard_input("打开QQ")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        time.sleep(3)
        # 断言
        assert self.driver.current_activity == ".activity.LoginActivity"
    #多伦回答，最后一轮回答出现点赞点踩(点踩)
    def test_click_like_dislike08(self):
        time.sleep(2)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“你好”
        self.page.sessionpage.input_keyboard_input("灵魂六问")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        time.sleep(8)
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.like_dislike_text) == "本次回答满意吗？"
        # 点击点踩按钮
        self.page.sessionpage.click_dislike_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.dislike_text) == "哎呀，抱歉，我会再努力的~"

    #无意义的query，不出现点踩点赞
    def test_click_like_dislike09(self):
        time.sleep(2)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“你好”
        self.page.sessionpage.input_keyboard_input("帮我找一下手机")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        time.sleep(3)

        #断言
        assert self.page.sessionpage.is_button_exist(self.page.sessionpage.like_button)

    # 第三方技能，不出现点赞点踩
    def test_click_like_dislike10(self):
        time.sleep(2)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“你好”
        self.page.sessionpage.input_keyboard_input("数字对战")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        time.sleep(3)
        # 断言
        assert self.page.sessionpage.is_button_exist(self.page.sessionpage.like_button)

    # 8.29新增（刘锐）
    # 小卡布局改动：query：今天天气，出现天气小卡，卡片技能条由卡片底部转移到卡片上部
    def test_click_like_dislike11(self):
        time.sleep(2)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“你好”
        self.page.sessionpage.input_keyboard_input("今天天气")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        time.sleep(3)
        #点赞
        self.page.sessionpage.click_like_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.small_card_icon) == '小米天气'
        assert self.page.sessionpage.get_text(self.page.sessionpage.like_text) == "开心，我会再接再厉加油的！"

     # query：大自然的声音，点赞成功
    def test_click_like_dislike12(self):
        time.sleep(2)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“你好”
        self.page.sessionpage.input_keyboard_input("大自然的声音")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        time.sleep(3)
        #点赞
        self.page.sessionpage.click_like_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.small_card_icon) == '听声音'
        assert self.page.sessionpage.get_text(self.page.sessionpage.like_text) == "开心，我会再接再厉加油的！"

    # query：少年派是谁演的，点赞成功
    def test_click_like_dislike13(self):
        time.sleep(2)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“你好”
        self.page.sessionpage.input_keyboard_input("少年派是谁演的")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        time.sleep(3)
        #点赞
        self.page.sessionpage.click_like_button()
        #断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.small_card_icon) == '人物·视频'
        assert self.page.sessionpage.get_text(self.page.sessionpage.like_text) == "开心，我会再接再厉加油的！"

    # query：外婆的妹妹叫什么
    def test_click_like_dislike14(self):
        time.sleep(2)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“你好”
        self.page.sessionpage.input_keyboard_input("外婆的妹妹叫什么")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        time.sleep(3)
        #点赞
        self.page.sessionpage.click_like_button()
        # 断言
        # assert self.page.sessionpage.get_text(self.page.sessionpage.small_card_icon) == '计算器'
        assert self.page.sessionpage.get_text(self.page.sessionpage.like_text) == "开心，我会再接再厉加油的！"

# query：来首歌，点赞
    def test_click_like_dislike15(self):
        time.sleep(2)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“你好”
        self.page.sessionpage.input_keyboard_input("来首歌")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        time.sleep(3)
        #点赞
        self.page.sessionpage.click_like_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.small_card_icon) == 'QQ音乐'
        assert self.page.sessionpage.get_text(self.page.sessionpage.like_text) == "开心，我会再接再厉加油的！"

# query：电影
    def test_click_like_dislike16(self):
        time.sleep(2)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“你好”
        self.page.sessionpage.input_keyboard_input("电影")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        time.sleep(3)
        #点赞
        self.page.sessionpage.click_like_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.like_text) == "开心，我会再接再厉加油的！"