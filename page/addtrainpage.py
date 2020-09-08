import time

from selenium.webdriver.common.by import By

from base.base_action import BaseAction

# 添加设备页
class AddTrainPage(BaseAction):

    # 你对小爱说的话的输入框
    train_request_box = By.XPATH, "//*[@resource-id='QuestionPart']/android.view.View[1]/android.widget.EditText[1]"

    def input_train_request_box(self,text):
        self.input(self.train_request_box,text)

    # 新建训练-添加训练的按钮
    add_train_button = By.XPATH, '//*[@text="添加训练"]'

    def click_add_train_button(self):
        self.click(self.add_train_button)

    # 小爱回应的-一句话
    respone_one_word = By.XPATH, '//*[@text="一句话"]'

    def click_rerespone_one_word(self):
        self.click(self.respone_one_word)


    # #小爱回应的输入框
    train_reponse_box = By.XPATH,"//*[@resource-id='AnswerPart']/android.view.View[1]/android.view.View[2]/android.widget.EditText[1]"

    # 小爱回应的-一段录音
    onerecording = By.XPATH, '//*[@text="一段录音"]'
    # 进入录音界面的，开始录音按钮，结束录音也是这个
    soundrecording_button = By.ID, 'com.xiaomi.xiaoailite:id/btn_record'
    # // *[ @ resource - id = "com.xiaomi.xiaoailite:id/btn_record"
    # 录音完成的对勾
    record_done = By.ID, 'com.xiaomi.xiaoailite:id/btn_complete'
    # [765,1959][945,2139]
    # 小爱回应的-设备控制
    equipmentcontrol = By.XPATH, '//*[@text="设备控制"]'
    # 更多设置
    moresetup = By.XPATH, '//*[@text="更多设置"]'
    # //*[@resource-id="root"]/android.view.View[1]

    # 我的训练-示例或者新建训练计划右上角的三个点
    trainsetup = By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[3]'
    # [933,445][993,505]
    # trainsetup = By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[3]'
    # 三个点-编辑
    edit_button = By.XPATH, '//*[@text="编辑"]'
    # edit_button = By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.widget.ListView/android.view.View[1]/android.view.View'
    # 三个点-删除
    delect_button = By.XPATH, '//*[@text="删除"]'
    # 删除-弹框-确认
    ok_button = By.XPATH, '//*[@text="确定"]'
    # 删除-弹框-取消
    no_button = By.XPATH, '//*[@text="取消"]'
    # 新建训练-添加训练的按钮
    addtrain_button = By.XPATH, '//*[@text="添加训练"]'

    def input_train_reponse_box(self,text):
        self.input(self.train_reponse_box,text)

    # 点击小爱的回应-一段录音
    def click_onerecording(self):
        self.find_element_with_scroll(self.onerecording).click()

    # 点击小爱的回应-一段录音-录音的按钮
    def click_soundrecording_button(self):
        self.click(self.soundrecording_button)
        #[450,1959][630,2139]
    #点击小爱的回应-一段录音-录音的按钮-录音完成的对勾
    def click_record_done(self):
        self.click(self.record_done)
    #     # 点击小爱的回应-设备控制
    def click_equipmentcontrol(self):
        self.find_element_with_scroll(self.equipmentcontrol).click()
    #点击更多设置
    def click_moresetup(self):
        self.find_element_with_scroll(self. moresetup).click()
    #点击-我的训练-示例或者新建训练计划右上角的三个点
    def click_trainsetup(self):
        self.find_element_with_scroll(self.trainsetup).click()
    #点击-三个点-编辑
    def click_edit_button(self):
        # self.find_element_with_scroll(self.edit_button).click()
        self.click(self.edit_button)
    #点击-三个点-删除
    def click_delect_button(self):
        self.find_element_with_scroll(self.delect_button).click()
#点击-三个点-删除-弹框-确认
    def click_ok_button(self):
        self.click(self.ok_button)
## 点击新建训练中的添加训练按钮
    def click_addtrain_button(self):
        self.click(self.addtrain_button)