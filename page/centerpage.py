import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

from base.base_action import BaseAction

# 个人中心页
class CenterPage(BaseAction):

    # 页面标题“个人中心”
    tittle = By.ID,"com.xiaomi.xiaoailite:id/toolbar_title"

    # 返回按钮
    back_button = By.XPATH, "//android.widget.ImageButton"

    # 登录tab按钮
    login_tab = By.ID,"com.xiaomi.xiaoailite:id/tv_user_name"

    # 对话记录按钮
    history_record_button = By.ID, "com.xiaomi.xiaoailite:id/tv_history_record"

    # 我的训练
    my_train = By.ID, "com.xiaomi.xiaoailite:id/tv_training_plan"

    # 我的奖品
    my_prize = By.ID, "com.xiaomi.xiaoailite:id/tv_my_prize"

    # 个人中心-小爱实验室
    xiaoai_lab = By.ID, "com.xiaomi.xiaoailite:id/tv_laboratory"

    # 我的设备按钮
    my_device_button = By.ID, "com.xiaomi.xiaoailite:id/tv_my_device"

    # 设备指南
    device_guide_tab = By.ID, "com.xiaomi.xiaoailite:id/tv_device_instruction"

    ##个人中心-语音唤醒
    voice_wake_tab = By.ID, "com.xiaomi.xiaoailite:id/tv_voice_trigger"

    ##个人中心-连续对话设置
    continuous_session_tab = By.ID, "com.xiaomi.xiaoailite:id/tv_full_duplex"

    # 快捷方式tab
    shortcut_tab = By.ID, "com.xiaomi.xiaoailite:id/tv_shortcut"

    # 小爱建议tab
    xiaoai_suggest_tab = By.ID, "com.xiaomi.xiaoailite:id/iv_ai_suggestion_arrow"

    # 清理缓存
    clear_cache = By.ID, "com.xiaomi.xiaoailite:id/iv_clear_cache_arrow"

    ##个人中心-我的闹钟
    my_alarm = By.ID, "com.xiaomi.xiaoailite:id/tv_my_alarm"

    ##个人中心-我的日程
    my_schedule_tab = By.ID, "com.xiaomi.xiaoailite:id/tv_my_calendar"

    # 问题反馈tab
    problem_feedback = By.XPATH, "//*[contains(@text,'问题反馈')]"

    # 个人中心-用户协议和隐私政策
    privacy_policy_tab = By.ID, "com.xiaomi.xiaoailite:id/tv_privacy_policy"

    # 个人中心-当前版本
    current_version = By.ID, "com.xiaomi.xiaoailite:id/tv_current_version_summary"

    # 点击后出现，再想想
    again_thing_btn = By.ID, "com.xiaomi.xiaoailite:id/btn_cancel"

    # 好的按钮
    ok_button = By.ID, "com.xiaomi.xiaoailite:id/btn_confirm"

    # 退出登录
    out_login = By.ID,"com.xiaomi.xiaoailite:id/tv_logout"


    # 点击登录tab
    def click_login_tab(self):
        self.click(self.login_tab)

    #    点击我的训练
    def click_my_train(self):
        self.click(self.my_train)

    # 点击我的奖品
    def click_my_prize(self):
        self.click(self.my_prize)

    # 点击小爱实验室
    def click_xiaoai_lab(self):
        self.click(self.xiaoai_lab)

    # 点击对话记录
    def click_history_record(self):
        self.click(self.history_record_button)
    # 点击返回按钮
    def click_back_button(self):
        self.click(self.back_button)
    #   点击我的设备
    def click_my_device_button(self):
        self.find_element_with_scroll(self.my_device_button).click()
    # 点击设备指南tab
    def click_device_guide_tab(self):
        self.find_element_with_scroll(self.device_guide_tab).click()
    # 点击语音唤醒
    def click_voice_wake_tab(self):
        self.find_element_with_scroll(self.voice_wake_tab).click()
    #   点击连续对话
    def click_continuous_session_tab(self):
        self.find_element_with_scroll(self.continuous_session_tab).click()
    # 点击“快捷方式”tab
    def click_shortcut_tab(self):
        self.find_element_with_scroll(self.shortcut_tab).click()
    # 点击"小爱建议"tab
    def click_xiaoai_suggest_tab(self):
        self.find_element_with_scroll(self.xiaoai_suggest_tab).click()
    #   点击清理缓存
    def click_clear_cache(self):
        self.find_element_with_scroll(self.clear_cache).click()
    # 获取清理缓存tab的文本
    def get_clear_cache_text(self):
        text = By.ID,"com.xiaomi.xiaoailite:id/tv_cache_size"
        return self.get_text(text)
    # 点击我的闹钟
    def click_my_alarm(self):
        self.find_element_with_scroll(self.my_alarm).click()
    #  点击我的日程
    def click_my_schedule_tab(self):
        self.find_element_with_scroll(self.my_schedule_tab).click()
    # 点击问题反馈
    def click_problem_feedback(self):
        self.find_element_with_scroll(self.problem_feedback).click()

    # 点击用户协议和隐私政策
    def click_privacy_policy_tab(self):
        self.find_element_with_scroll(self.privacy_policy_tab).click()
    #用户协议
    user_agreement =By.ID,'com.xiaomi.xiaoailite:id/tv_user_agreement'
    #隐私政策
    privacy_policy = By.ID,'com.xiaomi.xiaoailite:id/tv_privacy_policy'
    #点击用户协议
    def click_user_agreement(self):
        self.click(self.user_agreement)
    #点击隐私政策
    def click_provacy_policy(self):
        self.click(self.privacy_policy)
    # 点击退出登录
    def click_out_login(self):
        self.find_element_with_scroll(self.out_login).click()
    #    点击弹框"再想想"
    def click_again_thing_btn(self):
        self.click(self.again_thing_btn)
    #  点击弹框"好的"
    def click_ok_button(self):
        self.click(self.ok_button)

    # 获取当前版本信息文本
    def get_current_version_text(self):
        return self.find_element_with_scroll(self.current_version).text

    # 判断是否登录，登录：False,未登录：True
    def if_login(self):
        if "登录小米账号" == self.get_text(self.login_tab):
            return True
        return False





