import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

# 9.6 王茹楠
#快捷方式
class ShortCutPage(BaseAction):

    #返回按钮
    back_button=By.XPATH,"//*[contains(@resource-id,'toolbar')]//*[@index='0']"

    #快捷方式页面title
    stort_cut_title=By.ID,'com.xiaomi.xiaoailite:id/toolbar_title'

    #点击返回
    def click_back_button(self):
        self.click(self.back_button)


    # 课程表-添加tab
    school_timetable_add = By.XPATH,"//*[@text='添加' and @index='4']"


    # 课程表弹窗添加到主屏幕—--添加
    school_home_screen_add = By.XPATH,"//*[@text='添加']"
    school_home_screen_cancel = By.XPATH, "//*[@text='取消']"

    #确定按钮
    add_to_the_desktop_confirm = By.ID,'com.xiaomi.xiaoailite:id/btn_confirm'

    #点击课程表-添加
    def click_school_timetable_add(self):
        self.click(self.school_timetable_add)

    #点击添加到主屏幕—--添加课程表弹窗添加到主屏幕—--添加
    def click_school_home_screen_add(self):
        self.click(self.school_home_screen_add)

    #点击已尝试添加到桌面--确定
    def click_add_to_the_desktop_confirm(self):

        self.click(self.add_to_the_desktop_confirm)


        # 判断弹窗是否存在：True,没有弹窗：False
    def if_exist_pop_up_window(self):
        if "取消" == self.get_text(self.school_home_screen_cancel):
            return True
        return False









