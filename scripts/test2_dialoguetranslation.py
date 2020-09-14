# 对话翻译
import time

from appium.webdriver.common.touch_action import TouchAction

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

    # 9.6 尚景
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

    # 修改翻译内容，中文修改为中文
    def test_translation08(self):
        self.page.homepage.click_center_button()
        # 点击"小爱实验室"
        self.page.centerpage.click_xiaoai_lab()
        # 点击对话翻译
        self.page.xiaoailaboratorypage.click_dialoguetranslation_tap()
        # 输入要翻译的内容
        self.page.dialoguetranslationpage.input_translation_box("小爱翻译")
        # 点击翻译
        self.page.dialoguetranslationpage.click_Translation_button()
        # 点击修改内容按钮
        self.page.dialoguetranslationpage.click_src_text_edit()
        # 清空输入框
        self.page.dialoguetranslationpage.clean_input()
        # 输入翻译
        self.page.dialoguetranslationpage.input_et_text("更改文本")
        # 点击确定
        self.page.dialoguetranslationpage.click_btn_confirm()
        time.sleep(3)
        # 断言，页面可以找到更改文本的中文
        msg = self.page.dialoguetranslationpage.is_toast_exist("更改文本")
        # print(msg)
        assert msg is True


    # 修改翻译内容，中文修改为英文
    def test_translation09(self):
        self.page.homepage.click_center_button()
        # 点击"小爱实验室"
        self.page.centerpage.click_xiaoai_lab()
        # 点击对话翻译
        self.page.xiaoailaboratorypage.click_dialoguetranslation_tap()
        # 输入要翻译的内容
        self.page.dialoguetranslationpage.input_translation_box("小爱翻译")
        # 点击翻译
        self.page.dialoguetranslationpage.click_Translation_button()
        # 点击修改内容按钮
        self.page.dialoguetranslationpage.click_src_text_edit()
        # 清空输入框
        self.page.dialoguetranslationpage.clean_input()
        # 输入翻译
        self.page.dialoguetranslationpage.input_et_text("hello")
        # 点击确定
        self.page.dialoguetranslationpage.click_btn_confirm()
        time.sleep(3)
        # 断言
        msg = self.page.dialoguetranslationpage.is_toast_exist("hello")
        # print(msg)
        assert msg is True

    # 修改内容，不输入文字
    def test_translation10(self):
        self.page.homepage.click_center_button()
        # 点击"小爱实验室"
        self.page.centerpage.click_xiaoai_lab()
        # 点击对话翻译
        self.page.xiaoailaboratorypage.click_dialoguetranslation_tap()
        # 输入要翻译的内容
        self.page.dialoguetranslationpage.input_translation_box("小爱翻译")
        # 点击翻译
        self.page.dialoguetranslationpage.click_Translation_button()
        # 点击修改内容按钮
        self.page.dialoguetranslationpage.click_src_text_edit()
        # 清空输入框
        self.page.dialoguetranslationpage.clean_input()
        # 点击确定
        self.page.dialoguetranslationpage.click_btn_confirm()
        time.sleep(3)
        # 断言 获取toast  输入为空
        msg= self.page.dialoguetranslationpage.is_toast_exist("输入为空")
        # print(msg)
        assert msg is True

    # 修改内容，点击取消
    def test_translation11(self):
        self.page.homepage.click_center_button()
        # 点击"小爱实验室"
        self.page.centerpage.click_xiaoai_lab()
        # 点击对话翻译
        self.page.xiaoailaboratorypage.click_dialoguetranslation_tap()
        # 输入要翻译的内容
        self.page.dialoguetranslationpage.input_translation_box("小爱翻译")
        # 点击翻译
        self.page.dialoguetranslationpage.click_Translation_button()
        # 点击修改内容按钮
        self.page.dialoguetranslationpage.click_src_text_edit()
        # 清空输入框
        self.page.dialoguetranslationpage.clean_input()
        # 输入翻译
        self.page.dialoguetranslationpage.input_et_text("文本")
        # 点击取消
        self.page.dialoguetranslationpage.click_btn_cance()
        # 断言
        msg = self.page.dialoguetranslationpage.is_toast_exist("小爱翻译")
        # print(msg)
        assert msg is True

    # 修改目标语言，点击取消
    # 修改目标语言为日语，点击确定
    # 9.12何巧
    def test_translation06_copy(self):
        self.page.homepage.click_center_button()
        # 点击"小爱实验室"
        self.page.centerpage.click_xiaoai_lab()
        # 点击对话翻译
        self.page.xiaoailaboratorypage.click_dialoguetranslation_tap()
        # 输入要翻译的内容
        self.page.dialoguetranslationpage.input_translation_box("小爱同学")
        # 点击翻译
        self.page.dialoguetranslationpage.click_Translation_button()
        time.sleep(3)
        # 长按小爱同学
        self.page.dialoguetranslationpage.long_press(self.page.dialoguetranslationpage.XiaoAI)
        # 点击复制(元素定不到位，ID元素与小爱悬浮球的一样，选择了坐标）
        # self.page.dialoguetranslationpage.click_copy_button()
        # 点击复制
        TouchAction(self.driver).press(x=544, y=964).wait(3000).release().perform()
        # 断言-toast-这个toast有时可以获取，有时候不行，可以先用电脑尝试一下，如果不行，就注释assert这行，用肉眼判断通过
        assert self.page.dialoguetranslationpage.is_toast_exist("翻译内容已复制")

    # def test_translation07_delect(self):
    #     self.page.homepage.click_center_button()
    #     # 点击"小爱实验室"
    #     self.page.centerpage.click_xiaoai_lab()
    #     # 点击对话翻译
    #     self.page.xiaoailaboratorypage.click_dialoguetranslation_tap()
    #     # 输入要翻译的内容
    #     self.page.dialoguetranslationpage.input_translation_box("小爱同学")
    #     # 点击翻译
    #     self.page.dialoguetranslationpage.click_Translation_button()
    #     time.sleep(3)
    #     # 长按小爱同学
    #     self.page.dialoguetranslationpage.long_press(self.page.dialoguetranslationpage.XiaoAI)
    #     # # 点击删除(元素定不到位，选择了坐标）
    #     # self.page.dialoguetranslationpage.click_delect_button()
    #     # 点击删除 (因为元素不好定位，选择坐标）
    #     TouchAction(self.driver).press(x=544, y=1079).wait(3000).release().perform()
    #     # 断言-toast
    #     # self.page.dialoguetranslationpage.is_toast_exist("翻译内容已删除")

    def test_translation08_clear(self):
        self.page.homepage.click_center_button()
        # 点击"小爱实验室"
        self.page.centerpage.click_xiaoai_lab()
        # 点击对话翻译
        self.page.xiaoailaboratorypage.click_dialoguetranslation_tap()
        # 输入要翻译的内容
        self.page.dialoguetranslationpage.input_translation_box("小爱同学")
        # 点击翻译
        self.page.dialoguetranslationpage.click_Translation_button()
        time.sleep(3)
        # 长按小爱同学
        self.page.dialoguetranslationpage.long_press(self.page.dialoguetranslationpage.XiaoAI)
        # #点击清空(元素定位不到，选择坐标）
        # self.page.dialoguetranslationpage.click_empty_button()
        # 点击删除
        TouchAction(self.driver).press(x=544, y=1190).wait(3000).release().perform()
        # 点击-清空-确认
        self.page.dialoguetranslationpage.click_ok_button()
        # 断言-toast
        self.page.dialoguetranslationpage.is_toast_exist("翻译内容已清空")