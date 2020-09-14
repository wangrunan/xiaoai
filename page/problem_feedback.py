from selenium.webdriver.common.by import By

from base.base_action import BaseAction

# 刘锐 9.13
# 小爱实验室页
class Problem_Feedback(BaseAction):
    #反馈的设备/App
    devices_type = By.XPATH,"//android.widget.TextView[@resource-id='com.xiaomi.xiaoailite:id/tv_select_question_device_label']"
    #问题的类型
    problem_type = By.XPATH,"//android.widget.TextView[@resource-id='com.xiaomi.xiaoailite:id/tv_select_question_type_label']"
    #输入框
    et_question_content = By.XPATH,"//android.widget.EditText[@resource-id='com.xiaomi.xiaoailite:id/et_question_content']"

    #小爱同学lite
    xiaoai_lite =By.XPATH, "//android.widget.TextView[@text='小爱同学Lite']"
    #s18
    s18 = By.XPATH,"//android.widget.TextView[@text='小米小爱蓝牙音箱随身版']"
    #Air2
    Air2 = By.XPATH,"//android.widget.TextView[@text='小米真无线蓝牙耳机Air2']"

    #语音不播报
    voice_not_play = By.XPATH,"// android.widget.TextView[ @ text = '语音不播报']"
    #语音识别错误
    voice_error = By.XPATH,"//android.widget.TextView[@text='语音识别错误']"

    #同时发送问题日志开关
    send_log_button = By.ID,'com.xiaomi.xiaoailite:id/ctv_send_log'
    #提示信息
    text_message = By.ID,"com.xiaomi.xiaoailite:id/tv_question_feed_back_tips"
    #提交按钮
    commit_button = By.XPATH,"//android.widget.TextView[@resource-id='com.xiaomi.xiaoailite:id/btn_commit']"
    # 点击小爱同学lite
    def click_xiaoai_lite(self):
        self.find_element_with_scroll(self.xiaoai_lite).click()

    #点击s18
    def click_s18(self):
        self.click(self.s18)
    #点击语音不播报
    def click_voice_not_play(self):
        self.click(self.voice_not_play)

    # 点击反馈的设备/App
    def click_devices_type(self):
        self.click(self.devices_type)
    # 点击问题类型
    def click_problem_type(self):
        self.click(self.problem_type)

    #输入问题描述
    def input_et_question_content(self, message):
        self.input(self.et_question_content, message)
    # 点击同时发送问题日志开关
    def click_send_log_button(self):
        self.click(self.send_log_button)

    # 点击提交按钮
    def click_commit_button(self):
        self.find_element_with_scroll(self.commit_button).click()

