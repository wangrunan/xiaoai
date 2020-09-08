from selenium.webdriver.common.by import By

from base.base_action import BaseAction

# 我的设备页
class MyDevicePage(BaseAction):
    # 添加按钮+
    add_button = By.XPATH, '//*[@resource-id="com.xiaomi.xiaoailite:id/tv_toolbar_right"]'

    # 蓝牙设备tab
    BT_devices_tab = By.XPATH, '//*[@text="蓝牙设备"]'
    # 智能家居tab
    Smart_home_tab = By.XPATH, '//*[@text="智能家居"]'
    # 蓝牙设备-智能家居-添加设备/登录
    BTadd_button = By.ID, "com.xiaomi.xiaoailite:id/tv_button"
    # 选择弹框——好的
    ok_button = By.ID,"com.xiaomi.xiaoailite:id/btn_confirm"
    # 选择弹框-取消
    cancel_button = By.ID,"com.xiaomi.xiaoailite:id/btn_cancel"

    # 点击添加按钮
    def click_add_button(self):
        self.click(self.add_button)

    # 点击蓝牙设备tab
    def click_BT_devices_tab(self):
        self.click(self.BT_devices_tab)

    # 点击智能家居tab
    def click_Smart_home_tab(self):
        self.click(self.Smart_home_tab)

    # 蓝牙设备-智能家居-添加设备/登录
    def click_BTadd_button(self):
        self.click(self.BTadd_button)

    # 点击选择弹框-好的
    def click_ok_button(self):
        self.click(self.ok_button)

    # # 点击选择弹框-取消
    def click_cancel_button(self):
        self.click(self.cancel_button)