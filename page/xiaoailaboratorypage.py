from selenium.webdriver.common.by import By

from base.base_action import BaseAction

# 小爱实验室页
class XiaoaiLaboratoryPage(BaseAction):
    #对话翻译tab
    dialoguetranslation =By.XPATH, "//*[@text='对话翻译']"
    #课程表tab
    ClassScheduleCard = By.XPATH,"//*[@text='课程表']"
    #音色设置tab
    Voicesettings = By.XPATH,"//*[@text='音色设置']"
    #小爱悬浮球tab
    Littlelovefloatingball =By.XPATH,"//*[@text='小爱悬浮球']"
    #手机默认语音助手tab
    Defaultvoiceassistant = By.XPATH,"//*[@text='手机默认语音助手']"

    # 点击音色设置tab
    def click_Voicesettings_tap(self):
        self.click(self.Voicesettings)
# 点击小爱悬浮球tab
    def click_Littlelovefloatingball_tap(self):
        self.click(self.Littlelovefloatingball)
#9.6 何巧
# 点击对话翻译tab
    def click_dialoguetranslation_tap(self):
        self.click(self.dialoguetranslation)
