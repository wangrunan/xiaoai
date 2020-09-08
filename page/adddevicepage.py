import time

from selenium.webdriver.common.by import By

from base.base_action import BaseAction

# 添加设备页
class AddDeicePage(BaseAction):

    # 购买设备按钮
    pay_device_button = By.ID,"com.xiaomi.xiaoailite:id/tv_toolbar_right"

    # 米家
    mi_jia= By.XPATH,'//*[@text="去米家添加更多设备"]'
    # 耳机类
    Earphones_tab = By.XPATH, '//*[@text="耳机类"]'
    # 音箱类
    Sound_box_tab = By.XPATH, '//*[@text="音箱类"]'
    # 其他设备
    Other_equipment_tab = By.XPATH, '//*[@text="其他设备"]'

    # Mi_Air2_pro耳机
    # Mi_Air2_pro = By.XPATH, '//*[@text="Mi Air2 pro"]'

    # # Mi Air2 Pro耳机
    Mi_Air2_Pro = By.XPATH, '//*[@text="Mi Air2 pro"]'

    # 悦米蓝牙音箱
    yuemi_Sound_box = By.XPATH, '//*[@text="悦米小爱随身音箱"]'

    # 去米家添加更多设备
    mi_home_add_more_device = By.XPATH, '//*[@text="去米家添加更多设备"]'

    # 添加设备页标题
    add_device_tittle = By.ID,"com.xiaomi.xiaoailite:id/toolbar_title"

    # 点击购买设备按钮
    def click_pay_device_button(self):
        self.click(self.pay_device_button)

        # 点击米家
    def click_mi_jia(self):
        self.find_element_with_scroll(self.mi_jia).click()

        # 点击耳机类
    def click_Earphones_tab(self):
        self.click(self.Earphones_tab)
        # 点击音箱类
    def click_Sound_box_tab(self):
        self.click(self.Sound_box_tab)
        # 点击其他设备
    def click_Other_equipment_tab(self):
        self.click(self.Other_equipment_tab)