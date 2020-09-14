# 问题反馈刘锐新增
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
#刘锐 9.13

    #点击问题反馈，跳转登录页面，不选择设备，直接点击提交,toast:请选择反馈的设备/App
    def test_click_null_01(self):
        # 首页点击个人中心按钮
        self.page.homepage.click_center_button()
        # 判断是否登录
        if self.page.centerpage.if_login():  # 登录：False,未登录：True
            # 点击问题反馈tab
            self.page.centerpage.click_problem_feedback()
            # 点击弹框"好的"按钮
            self.page.centerpage.click_ok_button()
            time.sleep(3)
            # 输入账号
            self.page.loginpage.input_user("13223015595")
            # 输入密码
            self.page.loginpage.input_password("123456qwerdf")
            # 点击登录
            self.page.loginpage.click_login_button()
            time.sleep(2)
            #点击问题反馈
            self.page.centerpage.click_problem_feedback()
            #模拟按键盘返回
            self.driver.press_keycode(4)
            #点击提交按钮
            self.page.problemfeedback.click_commit_button()
            #断言
            assert self.page.problemfeedback.is_toast_exist('设备')
            return
        # 已登录，# 点击问题反馈
        self.page.centerpage.click_problem_feedback()
        self.driver.press_keycode(4)
        # 点击提交按钮
        self.page.problemfeedback.click_commit_button()
        # 断言
        assert self.page.problemfeedback.is_toast_exist('设备')

 # 点击问题反馈，跳转登录页面,不选择设备，点击问题类型,toast:请选择反馈的设备/App
    def test_click__problem_type(self):
        # 首页点击个人中心按钮
        self.page.homepage.click_center_button()
        # 判断是否登录
        if self.page.centerpage.if_login():  # 登录：False,未登录：True
            # 点击问题反馈tab
            self.page.centerpage.click_problem_feedback()
            # 点击弹框"好的"按钮
            self.page.centerpage.click_ok_button()
            time.sleep(3)
            # 输入账号
            self.page.loginpage.input_user("13223015595")
            # 输入密码
            self.page.loginpage.input_password("123456qwerdf")
            # 点击登录
            self.page.loginpage.click_login_button()
            time.sleep(2)
            # 点击问题反馈
            self.page.centerpage.click_problem_feedback()
            self.driver.press_keycode(4)
            #点击问题类型
            self.page.problemfeedback.click_problem_type()
            # 断言
            assert self.page.problemfeedback.is_toast_exist('设备')
            return
        # 已登录，# 点击问题反馈
        self.page.centerpage.click_problem_feedback()
        self.driver.press_keycode(4)
        # 断言
        assert self.page.problemfeedback.is_toast_exist('设备')

    # 点击问题反馈，跳转登录页面,选择小爱同学Lite,点击提交，toast：请选择问题的类型
    def test_click_xiaoailite_03(self):
        # 首页点击个人中心按钮
        self.page.homepage.click_center_button()
        # 判断是否登录
        if self.page.centerpage.if_login():  # 登录：False,未登录：True
            # 点击问题反馈tab
            self.page.centerpage.click_problem_feedback()
            # 点击弹框"好的"按钮
            self.page.centerpage.click_ok_button()
            time.sleep(3)
            # 输入账号
            self.page.loginpage.input_user("13223015595")
            # 输入密码
            self.page.loginpage.input_password("123456qwerdf")
            # 点击登录
            self.page.loginpage.click_login_button()
            time.sleep(2)
            #点击问题反馈
            self.page.centerpage.click_problem_feedback()
            #点击小爱lite
            self.page.problemfeedback.click_xiaoai_lite()
            #点击提交按钮
            self.page.problemfeedback.click_commit_button()
            #断言
            assert self.page.problemfeedback.is_toast_exist('问题的类型')
            return
        # 已登录，# 点击问题反馈
        self.page.centerpage.click_problem_feedback()
        # 点击小爱lite
        self.page.problemfeedback.click_xiaoai_lite()
        # 点击提交按钮
        self.page.problemfeedback.click_commit_button()
        # 断言
        assert self.page.problemfeedback.is_toast_exist('问题的类型')

# 点击问题反馈，跳转登录页面,选择小爱同学Lite,选择语音不播报，输入框输入123456，关闭同时发送开关，点击提交，toast：反馈成功
    def test_04(self):
        # 首页点击个人中心按钮
        self.page.homepage.click_center_button()
        # 判断是否登录
        if self.page.centerpage.if_login():  # 登录：False,未登录：True
            # 点击问题反馈tab
            self.page.centerpage.click_problem_feedback()
            # 点击弹框"好的"按钮
            self.page.centerpage.click_ok_button()
            time.sleep(3)
            # 输入账号
            self.page.loginpage.input_user("13223015595")
            # 输入密码
            self.page.loginpage.input_password("123456qwerdf")
            # 点击登录
            self.page.loginpage.click_login_button()
            time.sleep(2)
            #点击问题反馈
            self.page.centerpage.click_problem_feedback()
            #点击小爱lite
            self.page.problemfeedback.click_xiaoai_lite()
            #点击问题类型
            self.page.problemfeedback.click_problem_type()
            #点击语音不播报
            self.page.problemfeedback.click_voice_not_play()
            #输入：123456
            self.page.problemfeedback.input_et_question_content('123456')
            #点击同时发送问题日志开关(关闭开关)
            self.page.problemfeedback.click_send_log_button()
            #点击提交按钮
            self.page.problemfeedback.click_commit_button()
            #断言
            assert self.page.centerpage.is_toast_exist('反馈成功')
            return
        # 已登录，# 点击问题反馈
        # 点击问题反馈
        self.page.centerpage.click_problem_feedback()
        # 点击小爱lite
        self.page.problemfeedback.click_xiaoai_lite()
        # 点击问题类型
        self.page.problemfeedback.click_problem_type()
        # 点击语音不播报
        self.page.problemfeedback.click_voice_not_play()
        # 输入：123456
        self.page.problemfeedback.input_et_question_content("123456")
        # 点击同时发送问题日志开关(关闭开关)
        self.page.problemfeedback.click_send_log_button()
        # 点击提交按钮
        self.page.problemfeedback.click_commit_button()
        # 断言
        assert self.page.centerpage.is_toast_exist('反馈成功')





