from selenium.webdriver.common.by import By

from base.base_action import BaseAction

# 小爱建议页
class SuggestPage(BaseAction):
    #页面标题
    suggest_tittle = By.ID,"com.xiaomi.xiaoailite:id/toolbar_title"

    #课程建议tab
    class_suggest_tab = By.XPATH,"//*[@text='课程建议']"

    def click_class_suggest_tab(self):
        self.click(self.class_suggest_tab)

    #天气变化建议tab
    weather_suggest_tab = By.XPATH,"//*[@text='天气变化']"

    def click_weather_suggest_tab(self):
        self.click(self.weather_suggest_tab)

    #智能环境建议tab
    intelligent_suggest_tab = By.XPATH,"//*[@text='智能环境建议']"

    def click_intelligent_suggest_tab(self):
        self.click(self.intelligent_suggest_tab)


    #课程建议页面标题
    class_page_tittle = By.XPATH,"//*[@text='课程']"

    #天气变化建议页面标题
    weather_suggest_page_tittle =  By.XPATH,"//*[@text='天气变化建议']"

    # 智能环境建议页面标题
    intelligent_suggest_page_tittle = By.XPATH, "//*[@text='智能环境建议']"

