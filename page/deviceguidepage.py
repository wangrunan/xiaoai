import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from base.base_action import BaseAction

#设备指南页
class DeviceGuidePage(BaseAction):

    # 设备指南页标题
    device_guide_tittle = By.ID,"com.xiaomi.xiaoailite:id/toolbar_title"

    # 如何添加设备tab
    add_device_tab = By.XPATH,"//*[@text='如何添加设备']"

    # 如何添加设备页标题
    add_device_tittle = By.ID,"com.xiaomi.xiaoailite:id/toolbar_title"

    # 添加设备失败怎么办tab
    add_device_fail_tab = By.XPATH, "//*[@text='添加设备失败怎么办']"

    # 添加设备失败怎么办页标题
    add_device_fail_tittle = By.ID, "com.xiaomi.xiaoailite:id/toolbar_title"

    # 如何删除设备tab
    delete_device_tab = By.XPATH, "//*[@text='如何删除设备']"

    # 如何删除设备页标题
    delete_device_tittle = By.ID, "com.xiaomi.xiaoailite:id/toolbar_title"

    # 设备重命名tab
    rename_device_tab = By.XPATH, "//*[@text='设备重命名']"

    # 设备重命名页标题
    rename_device_tittle = By.ID, "com.xiaomi.xiaoailite:id/toolbar_title"

    # 蓝牙设备升级tab
    device_upgrade_tab = By.XPATH, "//*[@text='蓝牙设备升级']"

    # 蓝牙设备升级页标题
    device_upgrade_tittle = By.ID, "com.xiaomi.xiaoailite:id/toolbar_title"

    # 查看当前支持设备tab
    current_support_device_tab = By.XPATH, "//*[@text='查看当前支持的设备']"

    # 查看当前支持设备页标题
    current_support_device_tittle = By.ID, "com.xiaomi.xiaoailite:id/toolbar_title"


    #   点击如何添加设备tab
    def click_add_device_tab(self):
        self.click(self.add_device_tab)
    #   点击添加设备失败怎么办tab
    def click_add_device_fail_tab(self):
        self.click(self.add_device_fail_tab)
    #   点击如何删除设备tab
    def click_delete_device_tab(self):
        self.click(self.delete_device_tab)
    #   点击设备重命名tab
    def click_rename_device_tab(self):
        self.click(self.rename_device_tab)
    #   点击蓝牙设备升级tab
    def click_device_upgrade_tab(self):
        self.click(self.device_upgrade_tab)
    #   点击查看当前支持设备tab
    def click_current_support_device_tab(self):
        self.click(self.current_support_device_tab)

