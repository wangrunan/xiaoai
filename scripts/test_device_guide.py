import time

from base.base_action import BaseAction
from base.driver import get_driver
from page.page import Page


class TestDeviceGuide:
    def setup(self):
        self.driver = get_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    #   点击如何添加设备tab
    def test_click_add_device_tab(self):
        #     首页点击个人中心按钮
        self.page.homepage.click_center_button()
        # 个人中心页点击设备指南
        self.page.centerpage.click_device_guide_tab()
        # 设备指南页点击如何添加设备tab
        self.page.deviceguidepage.click_add_device_tab()
        time.sleep(3)
        # 断言
        assert self.page.deviceguidepage.get_text(self.page.deviceguidepage.add_device_tittle) == "如何添加设备"

    #   点击添加设备失败怎么办tab
    def test_click_add_device_fail_tab(self):
        #     首页点击个人中心按钮
        self.page.homepage.click_center_button()
        # 个人中心页点击设备指南
        self.page.centerpage.click_device_guide_tab()
        # 设备指南页点 点击添加设备失败怎么办tab
        self.page.deviceguidepage.click_add_device_fail_tab()
        time.sleep(3)
        # 断言
        assert self.page.deviceguidepage.get_text(self.page.deviceguidepage.add_device_fail_tittle)  == "添加设备失败怎么办"


    #   点击如何删除设备tab
    def test_click_delete_device_tab(self):
        #     首页点击个人中心按钮
        self.page.homepage.click_center_button()
        # 个人中心页点击设备指南
        self.page.centerpage.click_device_guide_tab()
        # 设备指南页点击如何删除设备tab
        self.page.deviceguidepage.click_delete_device_tab()
        # 断言
        assert self.page.deviceguidepage.get_text(self.page.deviceguidepage.delete_device_tittle) == "如何删除设备"


    #   点击设备重命名tab
    def test_click_rename_device_tab(self):
        #     首页点击个人中心按钮
        self.page.homepage.click_center_button()
        # 个人中心页点击设备指南
        self.page.centerpage.click_device_guide_tab()
        # 设备指南页点击设备重命名tab
        self.page.deviceguidepage.click_rename_device_tab()
        # 断言
        assert self.page.deviceguidepage.get_text(self.page.deviceguidepage.rename_device_tittle)  == "设备重命名"


    #   点击蓝牙设备升级tab
    def test_click_device_upgrade_tab(self):
        #     首页点击个人中心按钮
        self.page.homepage.click_center_button()
        # 个人中心页点击设备指南
        self.page.centerpage.click_device_guide_tab()
        # 设备指南页点击蓝牙设备升级tab
        self.page.deviceguidepage.click_device_upgrade_tab()
        # 断言
        assert self.page.deviceguidepage.get_text(self.page.deviceguidepage.device_upgrade_tittle) == "蓝牙设备升级"


    #   点击查看当前支持设备tab
    def test_click_current_support_device_tab(self):
        #     首页点击个人中心按钮
        self.page.homepage.click_center_button()
        # 个人中心页点击设备指南
        self.page.centerpage.click_device_guide_tab()
        # 设备指南页点击查看当前支持设备tab
        self.page.deviceguidepage.click_current_support_device_tab()
        # 断言
        assert self.page.deviceguidepage.get_text(self.page.deviceguidepage.current_support_device_tittle) == "添加设备"
