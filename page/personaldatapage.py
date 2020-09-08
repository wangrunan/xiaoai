from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

from base.base_action import BaseAction

#个人资料页
class PersonalDataPage(BaseAction):

    #    个人信息页标题
    person_infoemation_tittle = By.ID,"fixedTitle"

    #     手机号tab
    phone_tab = By.XPATH,"//*[@text='手机号']"

    # 手机号页面标题
    phone_tittle = By.ID,"bigTitle"

    #     常用地址tab
    address_tab = By.XPATH, "//*[@text='常用地址']"

    # 常用地址页面标题
    address_tittle = By.ID, "bigTitle"

    #     出行信息tab
    trip_tab = By.XPATH, "//*[@text='出行信息']"

    # 出行信息页面标题
    trip_tittle = By.ID, "bigTitle"

    #     儿童信息tab
    child_tab = By.XPATH, "//*[@text='儿童信息']"

    # 儿童信息页面标题
    child_tittle = By.ID, "bigTitle"

    #     音乐偏好tab
    music_tab = By.XPATH, "//*[@text='音乐偏好']"

    # 音乐偏好页面标题
    music_tittle = By.ID, "bigTitle"

    # 点击手机号tab
    def click_phone_tab(self):
        self.find_element_with_scroll(self.phone_tab).click()
    # 点击常用地址tab
    def click_address_tab(self):
        self.find_element_with_scroll(self.address_tab).click()
    # 点击出行信息tab
    def click_trip_tab(self):
        self.find_element_with_scroll(self.trip_tab).click()
    # 点击儿童信息tab
    def click_child_tab(self):
        self.find_element_with_scroll(self.child_tab).click()
    # 点击音乐偏好tab
    def click_music_tab(self):
        self.find_element_with_scroll(self.music_tab).click()





