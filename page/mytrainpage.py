import time

from selenium.webdriver.common.by import By

from base.base_action import BaseAction

# 我的训练页
class MyTrainPage(BaseAction):

    # 返回按钮
    back_button = By.XPATH,"//android.widget.ImageButton[@content-desc='转到上一层级']"

    # "我的训练"标题
    tittle = By.ID,"com.xiaomi.xiaoailite:id/toolbar_title"

    # 点击返回
    def click_back_button(self):
        self.click(self.back_button)

    # 添加训练按钮
    add_training_button = By.XPATH, '//*[@text="添加训练"]'

    def click_add_training_button(self):
        self.click(self.add_training_button)