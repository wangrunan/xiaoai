import json
import time

import pytest

import config
from base.driver import get_driver
from page.page import Page


def get_data():
    test_data = []
    with open(config.path+"\data\login.json",encoding='UTF-8')as f:
        json_data = json.load(f) #将文件中的json数据读取出来
    list = json_data["login_data"]
    for a in list:
        test_data.append((a.get("username"),
                          a.get("pwd"),
                          a.get("expect"))
                         )  #在列表末尾添加新元素
    return test_data


class TestLogin:
    def setup(self):
        self.driver = get_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()


    # 登录失败
    @pytest.mark.parametrize("username,password,expect", get_data())
    def test_login_01(self,username, password, expect):
        # 点击个人中心按钮
        self.page.homepage.click_center_button()
        # 判断是否登录
        if self.page.centerpage.if_login():  #登录：False,未登录：True
            # 未登录
            # 点击登录tab
            self.page.centerpage.click_login_tab()
            # 输入账号
            self.page.loginpage.input_user(username)
            # 输入密码
            self.page.loginpage.input_password(password)
            # 点击登录
            self.page.loginpage.click_login_button()
            # 断言
            assert self.page.loginpage.get_text(self.page.loginpage.error_hint) in expect
            return
        #  已登录，退出登录
        self.page.centerpage.click_out_login()
        # 点击 好的
        self.page.centerpage.click_ok_button()
        # 首页点击个人中心按钮
        self.page.homepage.click_center_button()
        # 点击登录tab
        self.page.centerpage.click_login_tab()
        # 输入账号
        self.page.loginpage.input_user(username)
        # 输入密码
        self.page.loginpage.input_password(password)
        # 点击登录
        self.page.loginpage.click_login_button()
        # 断言
        assert self.page.loginpage.get_text(self.page.loginpage.error_hint) in expect

    # 登录成功
    def test_login_02(self):
        # 点击个人中心按钮
        self.page.homepage.click_center_button()
        # 判断是否登录
        if self.page.centerpage.if_login():  #登录：False,未登录：True
            # 未登录
            # 点击登录tab
            self.page.centerpage.click_login_tab()
            # 输入账号
            self.page.loginpage.input_user("15527619642")
            # 输入密码
            self.page.loginpage.input_password("t1005033132")
            # 点击登录
            self.page.loginpage.click_login_button()
            # 断言
            assert self.page.centerpage.get_text(self.page.centerpage.tittle) == "个人中心"
            return
        #  已登录，退出登录
        self.page.centerpage.click_out_login()
        # 点击 好的
        self.page.centerpage.click_ok_button()
        # 首页点击个人中心按钮
        self.page.homepage.click_center_button()
        # 点击登录tab
        self.page.centerpage.click_login_tab()
        # 输入账号
        self.page.loginpage.input_user("15527619642")
        # 输入密码
        self.page.loginpage.input_password("t1005033132")
        # 点击登录
        self.page.loginpage.click_login_button()
        # 断言
        assert self.page.centerpage.get_text(self.page.centerpage.tittle) == "个人中心"



