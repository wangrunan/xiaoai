# 小爱翻译页面
from selenium.webdriver.common.by import By

from base.base_action import BaseAction

#首面
class TranslationPage(BaseAction):
    # 输入框
    language_input= By.ID, "com.xiaomi.xiaoailite:id/src_language_input"

    # 翻译按钮
    translation_btn = By.ID,"com.xiaomi.xiaoailite:id/start_translation_btn"

    # 翻译结果
    # 多元素使用同一个id，需要定位一组元素并选择索引为1的元素
    # resource - id = "com.xiaomi.xiaoailite:id/dest_text"
    dest_text = By.XPATH,"//*[@resource-id='com.xiaomi.xiaoailite:id/dest_text']"

    # 更改结果按钮
    src_text_edit = By.ID, "com.xiaomi.xiaoailite:id/src_text_edit"

    # 更改结果输入框
    et_input = By.ID,"com.xiaomi.xiaoailite:id/et_input"

    #确定按钮
    btn_confirm = By.ID,"com.xiaomi.xiaoailite:id/btn_confirm"

    #取消按钮
    btn_cance = By.ID,"com.xiaomi.xiaoailite:id/btn_cance"

    # 点击翻译框
    def click_language_input(self):
        self.click(self.language_input)

    # 输入内容
    def input_translation_text(self,msg):
        self.input(self.language_input,msg)

    # 点击翻译按钮
    def click_translation_btn(self):
        self.click(self.translation_btn)

    # 获取翻译结果并返回
    def ren_translation_results(self):
        return self.get_text(self.dest_text)