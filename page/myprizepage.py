from selenium.webdriver.common.by import By

from base.base_action import BaseAction

# 小爱建议页
class MyprizePage(BaseAction):
    #实物奖品

    Prizeinkind= By.XPATH,"//*[@text='实物奖品']"

    #红包奖品
    Redenvelopeprize = By.XPATH,"//*[@text='红包奖品']"
    #卡券奖品
    Cardvoucherprize = By.XPATH,"//*[@text='卡券奖品']"
    #页面标题
    # title = By.ID,"com.xiaomi.xiaoailite: id / toolbar_title"
    # title = By.XPATH,'/ *[@resource-id="com.xiaomi.xiaoailite:id/toolbar_title"]'
    title = By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView'

    #点击实物奖品
    def click_Prizeinkind_tab(self):
        self.click(self.Prizeinkind)
#点击红包奖品
    def click_Redenvelopeprize_tab(self):
        self.click(self.Redenvelopeprize)
#点击卡券奖品
    def click_Cardvoucherprize_tab(self):
        self.click(self.Cardvoucherprize)
#获取页面的标题的内容
    def get_title_text(self):
        return self.find_element6(self.title).text

