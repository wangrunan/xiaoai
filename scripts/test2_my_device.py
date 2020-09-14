import time

from base.driver import get_driver
from page.page import Page


class TestMyDevice:
    def setup(self):
        self.driver = get_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    #     我的设备页点击“+”按钮，跳转添加设备页  跑不了，需要改代码
    def test_my_device01(self):
        # 首页点击个人中心按钮
        self.page.homepage.click_center_button()
        # 个人中心页点击我的设备tab
        self.page.centerpage.click_my_device_button()
        # 我的设备页点击“+”按钮
        self.page.mydevicepage.click_add_button()
        time.sleep(3)
        # 断言
        assert self.page.adddeicepage.get_text(self.page.adddeicepage.add_device_tittle) == "添加设备"

    #     我的设备页-蓝牙设备-添加设备，跳转添加设备页
    def test_my_device02(self):
        # 首页点击个人中心按钮
        self.page.homepage.click_center_button()
        # 个人中心页点击我的设备tab
        self.page.centerpage.click_my_device_button()
        # 我的设备页点击 蓝牙设备-添加设备
        self.page.mydevicepage.click_BTadd_button()
        time.sleep(3)
        # 断言
        assert self.page.adddeicepage.get_text(self.page.adddeicepage.add_device_tittle) == "添加设备"

    #  （未登录）   我的设备页-智能家园-登录，跳转登录页面
    def test_my_device03(self):
        # 首页点击个人中心按钮
        self.page.homepage.click_center_button()
        # 判断是否登录
        if self.page.centerpage.if_login():  #登录：False,未登录：True
            # 个人中心页点击我的设备tab
            self.page.centerpage.click_my_device_button()
            # 我的设备页点击 智能家园
            self.page.mydevicepage.click_Smart_home_tab()
            # 我的设备页点击 智能家园-登录，跳转登录页面
            self.page.mydevicepage.click_BTadd_button()
            self.page.mydevicepage.click_ok_button()
            time.sleep(3)
            # 断言
            assert self.driver.current_activity == "com.xiaomi.passport.ui.internal.AddAccountActivity"
            return
        # 点击退出登录
        self.page.centerpage.click_out_login()
        # 点击好的
        self.page.centerpage.click_ok_button()
        # 首页点击个人中心按钮
        self.page.homepage.click_center_button()
        # 个人中心页点击我的设备tab
        self.page.centerpage.click_my_device_button()
        # 我的设备页点击 智能家园
        self.page.mydevicepage.click_Smart_home_tab()
        # 我的设备页点击 智能家园-登录，跳转登录页面
        self.page.mydevicepage.click_BTadd_button()
        self.page.mydevicepage.click_ok_button()
        time.sleep(3)
        # 断言
        assert self.driver.current_activity == "com.xiaomi.passport.ui.internal.AddAccountActivity"

    #  （登录）   我的设备页-智能家园-添加设备，跳转添加设备页
    def test_my_device04(self):
        # 首页点击个人中心按钮
        self.page.homepage.click_center_button()
        # 判断是否登录
        if self.page.centerpage.if_login():  # 登录：False,未登录：True
            # 登录
            self.page.centerpage.click_login_tab()
            # 登录页面登录
            self.page.loginpage.input_user("15527619642")
            self.page.loginpage.input_password("t1005033132")
            self.page.loginpage.click_login_button()
            # 个人中心页点击我的设备tab
            self.page.centerpage.click_my_device_button()
            # 我的设备页点击 智能家园
            self.page.mydevicepage.click_Smart_home_tab()
            # 我的设备页点击 智能家园-添加设备
            self.page.mydevicepage.click_BTadd_button()
            time.sleep(3)
            # 断言
            assert self.driver.current_activity == ".device.choosedevice.ChooseDeviceActivity"
            return
        # 个人中心页点击我的设备tab
        self.page.centerpage.click_my_device_button()
        # 我的设备页点击 智能家园
        self.page.mydevicepage.click_Smart_home_tab()
        # 我的设备页点击 智能家园-添加设备
        self.page.mydevicepage.click_BTadd_button()
        time.sleep(3)
        # 断言
        assert self.driver.current_activity == ".device.choosedevice.ChooseDeviceActivity"

    #     我的设备页-蓝牙设备-添加设备，跳转添加设备页，点击购买设备，跳转小爱商城页
    def test_my_device05(self):
        # 首页点击个人中心按钮
        self.page.homepage.click_center_button()
        # 个人中心页点击我的设备tab
        self.page.centerpage.click_my_device_button()
        # 我的设备页点击 蓝牙设备-添加设备
        self.page.mydevicepage.click_BTadd_button()
        # 添加设备页点击 购买设备，跳转我的商城页
        self.page.adddeicepage.click_pay_device_button()
        time.sleep(3)
        # 断言
        assert self.driver.current_activity == ".widgets.web.WebActivity"

    #     添加设备页页-全部设备-去米家添加更多设备，跳转米家app
    def test_my_device06(self):
        # 首页点击个人中心按钮
        self.page.homepage.click_center_button()
        # 个人中心页点击我的设备tab
        self.page.centerpage.click_my_device_button()
        # 我的设备页点击 蓝牙设备-添加设备
        self.page.mydevicepage.click_BTadd_button()
        # 添加设备页点击 全部设备-去米家添加更多设备
        self.page.adddeicepage.click_mi_jia()
        time.sleep(3)
        # 断言
        assert self.driver.current_activity == ".device.choosedevice.ChooseDeviceActivity"

    #     添加设备页页-耳机类
    def test_my_device07(self):
        # 首页点击个人中心按钮
        self.page.homepage.click_center_button()
        # 个人中心页点击我的设备tab
        self.page.centerpage.click_my_device_button()
        # 我的设备页点击 蓝牙设备-添加设备
        self.page.mydevicepage.click_BTadd_button()
        # 添加设备页点击 耳机类
        self.page.adddeicepage.click_Earphones_tab()

        # 断言
        assert self.page.adddeicepage.get_text(self.page.adddeicepage.Mi_Air2_Pro) == "Mi Air2 pro"

    #     添加设备页页-音箱类
    def test_my_device08(self):
        # 首页点击个人中心按钮
        self.page.homepage.click_center_button()
        # 个人中心页点击我的设备tab
        self.page.centerpage.click_my_device_button()
        # 我的设备页点击 蓝牙设备-添加设备
        self.page.mydevicepage.click_BTadd_button()
        # 添加设备页点击 音箱类
        self.page.adddeicepage.click_Sound_box_tab()
        # 断言
        assert self.page.adddeicepage.get_text(self.page.adddeicepage.yuemi_Sound_box) == "悦米小爱随身音箱"

    #     添加设备页页-其他设备
    def test_my_device09(self):
        # 首页点击个人中心按钮
        self.page.homepage.click_center_button()
        # 个人中心页点击我的设备tab
        self.page.centerpage.click_my_device_button()
        # 我的设备页点击 蓝牙设备-添加设备
        self.page.mydevicepage.click_BTadd_button()
        # 添加设备页点击 其他设备
        self.page.adddeicepage.click_Other_equipment_tab()
        # 断言
        assert self.page.adddeicepage.get_text(self.page.adddeicepage.mi_home_add_more_device) == "去米家添加更多设备"

    #     添加设备页页-其他设备-跳转米家
    def test_my_device10(self):
        # 首页点击个人中心按钮
        self.page.homepage.click_center_button()
        # 个人中心页点击我的设备tab
        self.page.centerpage.click_my_device_button()
        # 我的设备页点击 蓝牙设备-添加设备
        self.page.mydevicepage.click_BTadd_button()
        # 添加设备页点击 其他设备
        self.page.adddeicepage.click_Other_equipment_tab()
        # 添加设备页点击 其他设备-去米家添加更多设备   跳转米家
        self.page.adddeicepage.click_mi_jia()
        time.sleep(3)
        # 断言
        assert self.driver.current_activity == ".device.choosedevice.ChooseDeviceActivity"