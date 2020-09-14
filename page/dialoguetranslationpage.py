import time

from selenium.common.exceptions import TimeoutException

from base.base_action import BaseAction
from selenium.webdriver.common.by import By
#9.6 何巧
# 对话翻译页
class DialogueTranslationPage(BaseAction):

    # 中文翻译按钮位置
    Chinesetranslation_button = By.XPATH, "//*[contains(@text,'中文')]"
    #英语的翻译按钮
    Eenlishtranslation_button = By.ID, "com.xiaomi.xiaoailite:id/dest_language_bg"
    #//*[@resource-id="com.xiaomi.xiaoailite:id/dest_language_bg"]
    #输入翻译内容的输入框
    TranslationcontentInput = By.XPATH, "//*[contains(@text,'请输入想要翻译的词语或句子')]"
    #//*[@resource-id="com.xiaomi.xiaoailite:id/src_language_input"]
    #com.xiaomi.xiaoailite:id/src_language_input
    #中英文
    chinese_enlish_button =  By.ID, "com.xiaomi.xiaoailite:id/language_exchange"
    #三个点
    add_button = By.ID, "com.xiaomi.xiaoailite:id/iv_toolbar_more"
    # #翻译
    Translation_button = By.ID, "com.xiaomi.xiaoailite:id/start_translation_btn"
    #com.xiaomi.xiaoailite:id/start_translation_btn
    #Xpath://*[@resource-id="com.xiaomi.xiaoailite:id/start_translation_btn"]
    #小爱同学（因为我输入的是小爱同学，所以这里写的是小爱同学
    XiaoAI = By.XPATH, "//*[contains(@text,'小爱同学')]"
    #复制按钮 点不上，我选了坐标 复制（545，964）
    copy_button = By.XPATH, '//*[@text="复制"]'
    #com.xiaomi.xiaoailite:id/text
    #	543, 963
    #删除按钮 #（545，1079）
    delect_button = By.XPATH, '//*[@text="删除"]'
    # 		543, 1076
    #清空按钮-（545，1190）
    empty_button = By.XPATH, '//*[@text="清空"]'
    #	543, 1189

    # 更改结果按钮
    src_text_edit = By.ID, "com.xiaomi.xiaoailite:id/src_text_edit"

    # 更改结果输入框
    et_input = By.ID, "com.xiaomi.xiaoailite:id/et_input"

    # 确定按钮
    btn_confirm = By.ID, "com.xiaomi.xiaoailite:id/btn_confirm"

    # 取消按钮
    btn_cance = By.ID, "com.xiaomi.xiaoailite:id/btn_cancel"
    # com.xiaomi.xiaoailite:id/btn_cancel

    #点击中文翻译按钮
    def click_Chinesetranslation_button(self):
        self.click(self.Chinesetranslation_button)
    #点击英语的翻译按钮
    def click_Eenlishtranslation_button(self):
        self.click(self.Eenlishtranslation_button)

    # 清空的确认按钮
    ok_button = By.XPATH, '//*[@text="好的"]'

#输入要翻译的内容
    def input_translation_box(self,text):
        self.input(self.TranslationcontentInput,text)
# 点击翻译tab
    def click_Translation_button(self):
        self.click(self.Translation_button)
# 点击中英按钮
    def click_chinese_enlish_button(self):
        self.click(self.chinese_enlish_button)
# 点击复制按钮
    def click_copy_button(self):
        self.click(self.copy_button)
# 点击复制按钮
    def click_add_button(self):
        self.click(self.add_button)

    # 点击更改结果按钮
    def click_src_text_edit(self):
        self.click(self.src_text_edit)

    # 清空输入框内容
    def clean_input(self):
        self.clear_test(self.et_input)

    # 输入内容
    def input_et_text(self,text):
        self.input(self.et_input, text)

    # 点击确定
    def click_btn_confirm(self):
        self.click(self.btn_confirm)

    # 点击取消
    def click_btn_cance(self):
        self.click(self.btn_cance)

    # 点击清空的好的按钮
    def click_ok_button(self):
        self.click(self.ok_button)