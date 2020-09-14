import time

from base.base_action import BaseAction
from base.driver import get_driver
from page.page import Page


class TestPersonInformation:
    def setup(self):
        self.driver = get_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    # 点击手机号tab
    def test_click_phone_tab(self):
        # 首页点击个人中心按钮
        self.page.homepage.click_center_button()
        if self.page.centerpage.if_login():  #登录：False,未登录：True
            # 未登陆，登录账号
            self.page.centerpage.click_login_tab()
            self.page.loginpage.input_user("15527619642")
            self.page.loginpage.input_password("t1005033132")
            self.page.loginpage.click_login_button()
            time.sleep(3)
            # 个人中心页点击登录tab
            self.page.centerpage.click_login_tab()
            # 点击手机号tab
            self.page.personaldatapage.click_phone_tab()
            time.sleep(3)
            # 断言
            assert self.driver.current_activity == ".widgets.web.WebActivity"
            return
        # 已登录
        self.page.centerpage.click_login_tab()
        self.page.personaldatapage.click_phone_tab()
        time.sleep(3)
        # 断言
        assert self.driver.current_activity == ".widgets.web.WebActivity"

    # 点击常用地址tab
    def test_click_address_tab(self):
        # 首页点击个人中心按钮
        self.page.homepage.click_center_button()
        if self.page.centerpage.if_login():  #登录：False,未登录：True
            # 未登陆，登录账号
            self.page.centerpage.click_login_tab()
            self.page.loginpage.input_user("15527619642")
            self.page.loginpage.input_password("t1005033132")
            self.page.loginpage.click_login_button()
            time.sleep(3)
            # 个人中心页点击登录tab
            self.page.centerpage.click_login_tab()
            # 点击常用地址tab
            self.page.personaldatapage.click_address_tab()
            time.sleep(3)
            # 断言
            assert self.driver.current_activity == ".widgets.web.WebActivity"
            return
        # 已登录
        self.page.centerpage.click_login_tab()
        self.page.personaldatapage.click_address_tab()
        time.sleep(3)
        # 断言
        assert self.driver.current_activity == ".widgets.web.WebActivity"

    # 点击出行信息tab
    def test_click_trip_tab(self):
        # 首页点击个人中心按钮
        self.page.homepage.click_center_button()
        if self.page.centerpage.if_login():  #登录：False,未登录：True
            # 未登陆，登录账号
            self.page.centerpage.click_login_tab()
            self.page.loginpage.input_user("15527619642")
            self.page.loginpage.input_password("t1005033132")
            self.page.loginpage.click_login_button()
            time.sleep(3)
            # 个人中心页点击登录tab
            self.page.centerpage.click_login_tab()
            # 点击出行信息tab
            self.page.personaldatapage.click_trip_tab()
            time.sleep(3)
            # 断言
            assert self.driver.current_activity == ".widgets.web.WebActivity"
            return
        # 已登录
        self.page.centerpage.click_login_tab()
        self.page.personaldatapage.click_trip_tab()
        time.sleep(3)
        # 断言
        assert self.driver.current_activity == ".widgets.web.WebActivity"

    # 点击儿童信息tab
    def test_click_child_tab(self):
        # 首页点击个人中心按钮
        self.page.homepage.click_center_button()
        if self.page.centerpage.if_login():  #登录：False,未登录：True
            # 未登陆，登录账号
            self.page.centerpage.click_login_tab()
            self.page.loginpage.input_user("15527619642")
            self.page.loginpage.input_password("t1005033132")
            self.page.loginpage.click_login_button()
            time.sleep(3)
            # 个人中心页点击登录tab
            self.page.centerpage.click_login_tab()
            # 点击儿童信息tab
            self.page.personaldatapage.click_child_tab()
            time.sleep(3)
            # 断言
            assert self.driver.current_activity == ".widgets.web.WebActivity"
            return
        # 已登录
        self.page.centerpage.click_login_tab()
        self.page.personaldatapage.click_child_tab()
        time.sleep(3)
        # 断言
        assert self.driver.current_activity == ".widgets.web.WebActivity"

    # 点击音乐偏好tab
    def test_click_music_tab(self):
        # 首页点击个人中心按钮
        self.page.homepage.click_center_button()
        if self.page.centerpage.if_login():  #登录：False,未登录：True
            # 未登陆，登录账号
            self.page.centerpage.click_login_tab()
            self.page.loginpage.input_user("15527619642")
            self.page.loginpage.input_password("t1005033132")
            self.page.loginpage.click_login_button()
            time.sleep(3)
            # 个人中心页点击登录tab
            self.page.centerpage.click_login_tab()
            # 点击音乐偏好tab
            self.page.personaldatapage.click_music_tab()
            time.sleep(3)
            # 断言
            assert self.driver.current_activity == ".widgets.web.WebActivity"
            return
        # 已登录
        self.page.centerpage.click_login_tab()
        self.page.personaldatapage.click_music_tab()
        time.sleep(3)
        # 断言
        assert self.driver.current_activity == ".widgets.web.WebActivity"

    # 个人中心页点击登录tab
    def test_click_login_tab(self):
        # 首页点击个人中心按钮
        self.page.homepage.click_center_button()
        if self.page.centerpage.if_login():  # 登录：False,未登录：True
            # 未登陆，登录账号
            self.page.centerpage.click_login_tab()
            self.page.loginpage.input_user("15527619642")
            self.page.loginpage.input_password("t1005033132")
            self.page.loginpage.click_login_button()
            time.sleep(3)
            # 个人中心页点击登录tab
            self.page.centerpage.click_login_tab()
            time.sleep(3)
            # 断言
            assert self.driver.current_activity == ".widgets.web.WebActivity"
            return
        # 已登录
        self.page.centerpage.click_login_tab()
        time.sleep(3)
        # 断言
        assert self.driver.current_activity == ".widgets.web.WebActivity"


       #添加儿童信息，点击昵称，输入昵称的字数超过12个字的体醒
    def test_child_info1(self):
        # 首页点击个人中心按钮
        self.page.homepage.click_center_button()
        if self.page.centerpage.if_login():  # 登录：False,未登录：True
            # 未登陆，登录账号
            self.page.centerpage.click_login_tab()
            self.page.loginpage.input_user("15527619642")
            self.page.loginpage.input_password("t1005033132")
            self.page.loginpage.click_login_button()
            time.sleep(5)
            # 个人中心页点击登录tab
            self.page.centerpage.click_login_tab()
            # 点击儿童信息tab
            self.page.personaldatapage.click_child_tab()
            #点击添加新成员
            self.page.childinfopage.click_add_new_member()
            #点击昵称tab
            self.page.childinfopage.click_nick_name()
            #输入昵称字数超过12个
            self.page.childinfopage.input_nick_name("大家好我是小爱同学是大家的好伙伴")
            # 断言
            assert "最多可" in self.page.childinfopage.get_text(self.page.childinfopage.message_1)
            return
        # 个人中心页点击登录tab
        self.page.centerpage.click_login_tab()
        # 点击儿童信息tab
        self.page.personaldatapage.click_child_tab()
        # 点击添加新成员
        self.page.childinfopage.click_add_new_member()
        # 点击昵称tab
        self.page.childinfopage.click_nick_name()
        # 输入昵称字数超过12个
        self.page.childinfopage.input_nick_name("大家好我是小爱同学是大家的好伙伴")
        # 断言
        # assert "最多可" in self.page.childinfopage.get_text(self.page.childinfopage.message_1)
        assert self.page.childinfopage.is_toast_exist('最多可')

    # 添加儿童信息成功
    def test_child_info2(self):
        # 首页点击个人中心按钮
        self.page.homepage.click_center_button()
        if self.page.centerpage.if_login():  # 登录：False,未登录：True
            # 未登陆，登录账号
            self.page.centerpage.click_login_tab()
            self.page.loginpage.input_user("15527619642")
            self.page.loginpage.input_password("t1005033132")
            self.page.loginpage.click_login_button()
            time.sleep(5)
            # 个人中心页点击登录tab
            self.page.centerpage.click_login_tab()
                # 点击儿童信息tab
            self.page.personaldatapage.click_child_tab()
            # 添加新成员
            self.page.childinfopage.click_add_new_member()
            #点击昵称
            self.page.childinfopage.click_nick_name()
            #输入昵称
            self.page.childinfopage.input_nick_name("大大")
            # 点击弹框“确定”
            self.page.childinfopage.click_ok_button()
            # 点击对勾保存按钮
            self.page.childinfopage.click_done_button()
            assert self.page.childinfopage.is_toast_exist("保存成功")
            return
        # 个人中心页点击登录tab
        self.page.centerpage.click_login_tab()
        # 点击儿童信息tab
        self.page.personaldatapage.click_child_tab()
        # 添加新成员
        self.page.childinfopage.click_add_new_member()
        # 点击昵称
        self.page.childinfopage.click_nick_name()
        # 输入昵称
        self.page.childinfopage.input_nick_name("大大")
        # 点击弹框“确定”
        self.page.childinfopage.click_ok_button()
        # 点击对勾保存按钮
        self.page.childinfopage.click_done_button()
        assert self.page.childinfopage.is_toast_exist("保存成功")
    # 删除儿童信息  失败，需要重跑
    def test_child_info3(self):
        # 首页点击个人中心按钮
        self.page.homepage.click_center_button()
        if self.page.centerpage.if_login():  # 登录：False,未登录：True
            # 未登陆，登录账号
            self.page.centerpage.click_login_tab()
            self.page.loginpage.input_user("15527619642")
            self.page.loginpage.input_password("t1005033132")
            self.page.loginpage.click_login_button()
            time.sleep(3)
            # 个人中心页点击登录tab
            self.page.centerpage.click_login_tab()
            # 点击儿童信息tab
            self.page.personaldatapage.click_child_tab()
            # 长按
            self.page.childinfopage.long_press(self.page.childinfopage.DADA)
            # 点击删除
            self.page.childinfopage.click_delect_button()
            # 断言
            assert self.page.childinfopage.is_toast_exist("删除成功")
            return
        # 个人中心页点击登录tab
        self.page.centerpage.click_login_tab()
        # 点击儿童信息tab
        self.page.personaldatapage.click_child_tab()
        # 长按
        self.page.childinfopage.long_press(self.page.childinfopage.DADA)
        # 点击删除
        self.page.childinfopage.click_delect_button()
        # 断言
        assert self.page.childinfopage.is_toast_exist("删除成功")

    # 在音乐偏好里面选择喜欢的歌手，点击选好了，有保存成功的提醒
    def test_music_preference1(self):
        # 首页点击个人中心按钮
        self.page.homepage.click_center_button()
        if self.page.centerpage.if_login():  # 登录：False,未登录：True
            # 未登陆，登录账号
            self.page.centerpage.click_login_tab()
            self.page.loginpage.input_user("15527619642")
            self.page.loginpage.input_password("t1005033132")
            self.page.loginpage.click_login_button()
            time.sleep(3)
            # 个人中心页点击登录tab
            self.page.centerpage.click_login_tab()
            # 个人信息页点击音乐tab
            self.page.personaldatapage.click_music_tab()
            # 音乐偏好页面点击喜欢的歌手
            self.page.musicpreferencePage.click_favoritesinger()
            # 点击选好了
            self.page.musicpreferencePage.click_choice()
            # 断言
            assert self.page.musicpreferencePage.is_toast_exist("保存成功")
            return
        # 个人中心页点击登录tab
        self.page.centerpage.click_login_tab()
        # 个人信息页点击音乐tab
        self.page.personaldatapage.click_music_tab()
        # 音乐偏好页面点击喜欢的歌手
        self.page.musicpreferencePage.click_favoritesinger()
        # 点击选好了
        self.page.musicpreferencePage.click_choice()
        # 断言
        assert self.page.musicpreferencePage.is_toast_exist("保存成功")


    # 在音乐偏好里面选择喜欢的歌手的风格-嘻哈（没有选择），点击选好了，有保存成功的提醒
    def test_music_preference2(self):
        # 首页点击个人中心按钮
        self.page.homepage.click_center_button()
        if self.page.centerpage.if_login():  # 登录：False,未登录：True
            # 未登陆，登录账号
            self.page.centerpage.click_login_tab()
            self.page.loginpage.input_user("15527619642")
            self.page.loginpage.input_password("t1005033132")
            self.page.loginpage.click_login_button()
            time.sleep(3)
            # 个人中心页点击登录tab
            self.page.centerpage.click_login_tab()
            # 个人信息页点击音乐tab
            self.page.personaldatapage.click_music_tab()
            # 音乐偏好页面点击喜欢的歌曲风格
            self.page.musicpreferencePage.click_Favoritesongstyle()
            # 点击选好了
            self.page.musicpreferencePage.click_choice()
            # 断言
            assert self.page.musicpreferencePage.is_toast_exist("保存成功")
            return
        # 个人中心页点击登录tab
        self.page.centerpage.click_login_tab()
        # 个人信息页点击音乐tab
        self.page.personaldatapage.click_music_tab()
        # 音乐偏好页面点击喜欢的喜欢的歌曲风格
        self.page.musicpreferencePage.click_Favoritesongstyle()
        # 点击选好了
        self.page.musicpreferencePage.click_choice()
        # 断言
        assert self.page.musicpreferencePage.is_toast_exist("保存成功")


