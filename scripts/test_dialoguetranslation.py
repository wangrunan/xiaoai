import time

from base.base_action import BaseAction
from base.driver import get_driver
from page.page import Page


class TestDialoguetranslation:
    def setup(self):
        self.driver = get_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()
# 9.6 何巧
# # 小爱实验室里点击对话翻译-点击中文翻译
    def test_translation01_click_Chinesetranslation(self):
        self.page.homepage.click_center_button()
        # 点击"小爱实验室"
        self.page.centerpage.click_xiaoai_lab()
        #点击对话翻译
        self.page.xiaoailaboratorypage.click_dialoguetranslation_tap()
        # 点击点击中文翻译
        self.page.dialoguetranslationpage.click_Chinesetranslation_button()
        #断言-toast:抱歉，没有检测到有效的语音输入请靠近手机或大一点讲话
        self.page.dialoguetranslationpage.is_toast_exist("抱歉，没有检测到有效的语音输入请靠近手机或大一点讲话")
#小爱实验室里点击对话翻译-点击英文翻译
    def test_translation02_click_Eenlishtranslation(self):
        self.page.homepage.click_center_button()
        # 点击"小爱实验室"
        self.page.centerpage.click_xiaoai_lab()
        # 点击对话翻译
        self.page.xiaoailaboratorypage.click_dialoguetranslation_tap()
        #点击点击英文翻译
        self.page.dialoguetranslationpage.click_Eenlishtranslation_button()
        #断言-toast:抱歉，没有检测到有效的语音输入请靠近手机或大一点讲话
        self.page.xiaoailaboratorypage.is_toast_exist("抱歉，没有检测到有效的语音输入请靠近手机或大一点讲话")
#小爱实验室里点击对话翻译-点击想要输入的文字
    def test_translation03_input_translation(self):
        self.page.homepage.click_center_button()
        # 点击"小爱实验室"
        self.page.centerpage.click_xiaoai_lab()
        # 点击对话翻译
        self.page.xiaoailaboratorypage.click_dialoguetranslation_tap()
        #输入要翻译的内容
        self.page.dialoguetranslationpage.input_translation_box("小爱同学")
        #点击翻译
        self.page.dialoguetranslationpage.click_Translation_button()
        #断言-页面会有成功翻译出小爱同学的英文
        self.page.dialoguetranslationpage.is_toast_exist("XiaoAI")
#小爱实验室里点击对话翻译-点击中英按钮
    def test_translation04_click_chinese_enlish_button(self):
        self.page.homepage.click_center_button()
        # 点击"小爱实验室"
        self.page.centerpage.click_xiaoai_lab()
        # 点击对话翻译
        self.page.xiaoailaboratorypage.click_dialoguetranslation_tap()
        #点击中英按钮
        self.page.dialoguetranslationpage.click_chinese_enlish_button()
        #断言-页面会有成功翻译出小爱同学的英文
        self.page.dialoguetranslationpage.is_toast_exist("切换翻译语种")
#小爱实验室里点击对话翻译-点击三个点-有一个文字弹出
    def test_translation05_click_copy_button(self):
        self.page.homepage.click_center_button()
        # 点击"小爱实验室"
        self.page.centerpage.click_xiaoai_lab()
        # 点击对话翻译
        self.page.xiaoailaboratorypage.click_dialoguetranslation_tap()
        #点击三个点
        self.page.dialoguetranslationpage.click_add_button()
        #断言：添加小爱翻译到桌面的文字
        self.page.dialoguetranslationpage.is_toast_exist("添加小爱翻译到桌面")

 #9.6 尚景
 # 输入中文内容，进行翻译
    def test_input_chinese_translation(self):
        self.page.homepage.click_center_button()
        # 点击"小爱实验室"
        self.page.centerpage.click_xiaoai_lab()
        # 点击对话翻译
        self.page.xiaoailaboratorypage.click_dialoguetranslation_tap()
        # 输入要翻译的内容
        self.page.dialoguetranslationpage.input_translation_box("对话翻译")
        # 点击翻译
        self.page.dialoguetranslationpage.click_Translation_button()
        # 断言-页面会有成功翻译出对话翻译的英文
        self.page.dialoguetranslationpage.is_toast_exist("Dialogue")

    # 输入英文内容，进行翻译
    def test_input_english_translation(self):
        self.page.homepage.click_center_button()
        # 点击"小爱实验室"
        self.page.centerpage.click_xiaoai_lab()
        # 点击对话翻译
        self.page.xiaoailaboratorypage.click_dialoguetranslation_tap()
        # 输入要翻译的内容
        self.page.dialoguetranslationpage.input_translation_box("hello world")
        # 点击翻译
        self.page.dialoguetranslationpage.click_Translation_button()
        # 断言-页面会有成功翻译出hello world的中文
        self.page.dialoguetranslationpage.is_toast_exist("你好")