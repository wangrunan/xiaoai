import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from base.base_action import BaseAction

#音乐偏好页面
class MusicPreferencePage(BaseAction):

    # 喜欢的歌手
    favoritesinger= By.XPATH,'//*[@text="喜欢的歌手"]'
    #喜欢的歌曲风格
    Favoritesongstyle = By.XPATH,'//*[@text="喜欢的歌曲风格"]'
    #选好了
    choice = By.XPATH,'//*[@text="选好了"]'


    def click_favoritesinger(self):
        self.click(self.favoritesinger)

    def click_Favoritesongstyle(self):
        self.click(self.Favoritesongstyle)

    def click_choice(self):
        self.click(self.choice)



