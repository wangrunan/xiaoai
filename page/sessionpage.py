from selenium.webdriver.common.by import By

from base.base_action import BaseAction

# 对话页
class SessionPage(BaseAction):
    # 输入框
    keyboard_input = By.ID,"com.xiaomi.xiaoailite:id/et_input"

    # 发送按钮
    send_button = By.ID,"com.xiaomi.xiaoailite:id/iv_send"

    # 小卡icon图标
    small_card_icon = By.XPATH,"//*[@resource-id='com.xiaomi.xiaoailite:id/tv_skill_name']"

    # 大卡播放键
    big_card_play_button = By.XPATH,"//*[@resource-id='com.xiaomi.xiaoailite:id/iv_play_state']"

    # 大卡内容标题
    big_card_content_tittle = By.XPATH,"//*[@resource-id='com.xiaomi.xiaoailite:id/tv_title']"

    # 小卡内容标题
    small_card_content_tittle = By.ID,"com.xiaomi.xiaoailite:id/template_general_main_title"

    # 小卡内容
    samall_card_text = By.ID,"com.xiaomi.xiaoailite:id/template_general_text"

    # 大卡内容
    big_card_text = By.ID,"com.xiaomi.xiaoailite:id/template_general_text"

    # 大卡icon图标
    big_card_icon = By.XPATH,"//*[@resource-id='com.xiaomi.xiaoailite:id/tv_skill_name']"

    # tts回复
    tts_reply = By.XPATH,"//*[@resource-id='com.xiaomi.xiaoailite:id/tv_toast_view']"

    # 大卡tts回复
    big_card_tts_reply = By.ID,"com.xiaomi.xiaoailite:id/tv_large_card_toast"

    # 键盘输入内容
    def input_keyboard_input(self,message):
        self.input(self.keyboard_input,message)

    # 点击发送按钮
    def click_send_button(self):
        self.click(self.send_button)

    # 点击大卡暂停播放按钮
    def click_big_card_play_button(self):
        self.click(self.big_card_play_button)

    #点赞按钮
    like_button = By.ID,"com.xiaomi.xiaoailite:id/iv_like_icon"

    def click_like_button(self):
        self.click(self.like_button)


    # 点踩按钮
    dislike_button = By.ID,"com.xiaomi.xiaoailite:id/iv_dislike_icon"

    def click_dislike_button(self):
        self.click(self.dislike_button)

    # 点赞点踩选择文本
    like_dislike_text = By.ID,"com.xiaomi.xiaoailite:id/tv_prompt"

    # 点踩文本
    dislike_text = By.ID,"com.xiaomi.xiaoailite:id/tv_dislike_response"

    # 点赞文本
    like_text = By.ID,"com.xiaomi.xiaoailite:id/tv_like_response"

    # 翻译卡片的复制按钮
    card_copy_btn = By.ID, "com.xiaomi.xiaoailite:id/tv_copy"

    # 翻译卡片的对话翻译
    card_translation_btn = By.ID, "com.xiaomi.xiaoailite:id/tv_dialog_translation"
    # 翻译页面
    # 翻译标题
    translation_title = By.ID, "com.xiaomi.xiaoailite:id/toolbar_title"
    # 点翻译卡片的复制按钮
    def click_copy_btn(self):
        self.click(self.card_copy_btn)

    # 点击翻译卡片的对话翻译键
    def click_translation_btn(self):
        self.click(self.card_translation_btn)

    # 获取翻译卡片上的toast
    def ren_toast(self):
        return self.get_toast_text("译文已经复制")

    # 获取翻译标题
    def ren_translation_title(self):
        return self.get_text(self.translation_title)






