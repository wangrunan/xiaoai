import time

from base.base_action import BaseAction
from base.driver import get_driver
from page.page import Page


class TestSelfCenter:
    def setup(self):
        self.driver = get_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    # 点击对话记录
    def test_history_record(self):
        # 首页点击个人中心按钮
        self.page.homepage.click_center_button()
        #点击对话记录
        self.page.centerpage.click_history_record()
        #断言
        assert self.page.historyrecordpage.get_text(self.page.historyrecordpage.tittle) == "对话记录"

    # 未登录账号，点击我的训练按钮，跳转登录页面
    def test_click_my_train_1(self):
        # 首页点击个人中心按钮
        self.page.homepage.click_center_button()
        # 判断是否登录
        if self.page.centerpage.if_login():    #登录：False,未登录：True
            # 未登录,点击我的训练
            self.page.centerpage.click_my_train()
            # 点击弹框"好的"按钮
            self.page.centerpage.click_ok_button()
            time.sleep(3)
            # 断言
            assert self.driver.current_activity == "com.xiaomi.passport.ui.internal.AddAccountActivity"
            return
         # 已登录，点击退出登录
        self.page.centerpage.click_out_login()
        # 点击 好的
        self.page.centerpage.click_ok_button()
        # 首页点击个人中心按钮
        self.page.homepage.click_center_button()
        # 点击我的训练
        self.page.centerpage.click_my_train()
        # 点击弹框"好的"按钮
        self.page.centerpage.click_ok_button()
        # 断言
        assert self.driver.current_activity == "com.xiaomi.passport.ui.internal.AddAccountActivity"

    # 登录账号，点击我的训练按钮，跳转我的训练页面
    def test_click_my_train_2(self):
        # 首页点击个人中心按钮
        self.page.homepage.click_center_button()
        # 判断是否登录
        if self.page.centerpage.if_login():  # 登录：False,未登录：True
            # 如果未登录，点击我的训练
            self.page.centerpage.click_my_train()
            # 点击好的
            self.page.centerpage.click_ok_button()
            # 登录
            self.page.loginpage.input_user("15527619642")
            self.page.loginpage.input_password("t1005033132")
            self.page.loginpage.click_login_button()
            time.sleep(3)
            # 点击点击我的训练
            self.page.centerpage.click_my_train()
            time.sleep(3)
            #断言
            assert self.page.mytrainpage.get_text(self.page.mytrainpage.tittle) == "我的训练"
            return
        #已登录，点击我的训练
        self.page.centerpage.click_my_train()
        time.sleep(3)
        #断言
        assert self.page.mytrainpage.get_text(self.page.mytrainpage.tittle) == "我的训练"

    # 点击"我的奖品"按钮，跳转我的奖品页面
    def test_click_my_prize(self):
         # 首页点击个人中心按钮
        self.page.homepage.click_center_button()
        # 点击"我的奖品"按钮
        self.page.centerpage.click_my_prize()
        # 断言
        assert self.driver.current_activity == ".widgets.web.WebActivity"

    # 点击"小爱实验室"，跳转小爱实验室页面
    def test_click_xiaoai_lab(self):
        # 首页点击个人中心按钮
        self.page.homepage.click_center_button()
        # 点击"小爱实验室"
        self.page.centerpage.click_xiaoai_lab()
        # 断言
        assert self.driver.current_activity == ".presenter.activity.SettingLaboratoryActivity"


    # 点击我的设备tab，跳转是否正常
    def test_click_my_device(self):
        # 首页点击个人中心按钮
        self.page.homepage.click_center_button()
        # 点击我的设备tab
        self.page.centerpage.click_my_device_button()
        # 断言
        assert self.driver.current_activity == "com.xiaomi.bluetooth.activity.DeviceManagerLiteActivity"


    #     点击设备指南tab，跳转是否正常
    def test_device_guide(self):
        # 首页点击个人中心按钮
        self.page.homepage.click_center_button()
        # 点击设备指南tab
        self.page.centerpage.click_device_guide_tab()
        # 断言
        assert self.driver.current_activity == "com.xiaomi.bluetooth.activity.HelpActivity"

    # 点击语音唤醒tab，跳转是否正常
    def test_click_voice_wake(self):
        # 首页点击个人中心按钮
        self.page.homepage.click_center_button()
        # 点击语音唤醒tab
        self.page.centerpage.click_voice_wake_tab()
        # 断言
        assert self.driver.current_activity == ".presenter.activity.SettingVoiceWakeupActivity"

    # 点击连续对话设置,跳转是否正常
    def test_click_continuous_session_tab(self):
        # 首页点击个人中心按钮
        self.page.homepage.click_center_button()
        # 点击连续对话设置tab
        self.page.centerpage.click_continuous_session_tab()
        # 断言
        assert self.driver.current_activity == ".ai.fullduplex.FullDuplexActivity"

    # 点击"小爱建议"tab， 跳转是否正常
    def test_click_xiaoai_suggest_tab(self):
        # 首页点击个人中心按钮
        self.page.homepage.click_center_button()
        # 点击"小爱建议"tab
        self.page.centerpage.click_xiaoai_suggest_tab()
        # 断言
        assert self.driver.current_activity == ".presenter.activity.SettingAISuggestionActivity"

    # 清理缓存
    # def test_clear_cache(self):
    #     #首页点击个人中心按钮
    #     self.page.homepage.click_center_button()
    #     print(self.page.centerpage.get_clear_cache_text())
    #     # 判断清理缓存tab是否为oM
    #     if self.page.centerpage.get_clear_cache_text() == "OM":
    #         # 个人中心页点击清理缓存
    #         self.page.centerpage.click_clear_cache()
    #         print(self.driver.page_source)
    #         # 断言
    #         assert self.page.centerpage.is_toast_exist('没有什么可清理的了')
    #         return
    #     # 个人中心页点击清理缓存
    #     self.page.centerpage.click_clear_cache()
    #     # 点击弹框“好的”
    #     self.page.centerpage.click_ok_button()
    #     # 断言
    #     assert self.page.centerpage.is_toast_exist('清理完毕')

    # 点击我的闹钟
    def test_click_my_alarm(self):
        # 首页点击个人中心按钮
        self.page.homepage.click_center_button()
        # 点击我的闹钟
        self.page.centerpage.click_my_alarm()
        time.sleep(3)
        # 断言
        assert self.driver.current_activity == ".alarm.activity.AlarmWidgetListActivity"

    # 点击我的日程，跳转是否正常
    def test_click_my_schedule_tab(self):
        #         # 首页点击个人中心按钮
        self.page.homepage.click_center_button()
        # 点击"我的日程"tab
        self.page.centerpage.click_my_schedule_tab()
        time.sleep(3)
        print(self.driver.current_activity)
        # 断言
        assert self.driver.current_activity == "com.samsung.android.app.calendar.activity.MainActivity"

    # 点击问题反馈，跳转登录页面
    def test_click_problem_feedback(self):
        # 首页点击个人中心按钮
        self.page.homepage.click_center_button()
        # 判断是否登录
        if self.page.centerpage.if_login():  # 登录：False,未登录：True
            # 点击问题反馈tab
            self.page.centerpage.click_problem_feedback()
            # 点击弹框"好的"按钮
            self.page.centerpage.click_ok_button()
            time.sleep(3)
            # 断言
            assert self.driver.current_activity == "com.xiaomi.passport.ui.internal.AddAccountActivity"
            return
        # 已登录，退出登录
        self.page.centerpage.click_out_login()
        # 点击 好的
        self.page.centerpage.click_ok_button()
        # 首页点击个人中心按钮
        self.page.homepage.click_center_button()
        # 点击问题反馈tab
        self.page.centerpage.click_problem_feedback()
        # 点击弹框"好的"按钮
        self.page.centerpage.click_ok_button()
        time.sleep(3)
        # 断言
        assert self.driver.current_activity == "com.xiaomi.passport.ui.internal.AddAccountActivity"
        # self.page.centerpage.click_problem_feedback()
        # assert self.driver.current_activity == "com.xiaomi.bluetooth.activity.QuestionFeedBackActivity"

    # 点击"用户协议和隐私政策"tab，页面跳转是否正常
    def test_click_privacy_policy_tab(self):
        # 首页点击个人中心按钮
        self.page.homepage.click_center_button()
        # 点击"用户协议和隐私政策"tab
        self.page.centerpage.click_privacy_policy_tab()
        # 断言
        assert self.driver.current_activity == ".presenter.activity.UserPolicyActivity"

#9.6 刘锐
    #点击用户协议-用户协议页面
    def test_click_user_agreement(self):
        # 首页点击个人中心按钮
        self.page.homepage.click_center_button()
        # 点击"用户协议和隐私政策"tab
        self.page.centerpage.click_privacy_policy_tab()
        #点击用户协议
        self.page.centerpage.click_user_agreement()
        # 断言
        assert self.driver.current_activity == ".widgets.web.WebActivity"

    #点击隐私政策-隐私政策页面
    def test_click_privacy_policy(self):
        # 首页点击个人中心按钮
        self.page.homepage.click_center_button()
        # 点击"用户协议和隐私政策"tab
        self.page.centerpage.click_privacy_policy_tab()
        #点击隐私政策
        self.page.centerpage.click_provacy_policy()
        # 断言
        assert self.driver.current_activity == ".widgets.web.WebActivity"





