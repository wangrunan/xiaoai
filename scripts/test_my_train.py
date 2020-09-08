import time

from base.base_action import BaseAction
from base.driver import get_driver
from page.page import Page


class TestMyTrain:
    def setup(self):
        self.driver = get_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    # 新建训练页面不输入，点击添加训练，会有toast弹出
    def test_train01(self):
        # 首页点击个人中心按钮
        self.page.homepage.click_center_button()
        #判断登录
        if self.page.centerpage.if_login():  #登录：False,未登录：True
            # 未登录，点击登录
            self.page.centerpage.click_login_tab()
            self.page.loginpage.input_user("15527619642")
            self.page.loginpage.input_password("t1005033132")
            self.page.loginpage.click_login_button()
            time.sleep(3)
            #个人中心页点击我的训练
            self.page.centerpage.click_my_train()
            #我的训练页点击添加训练
            self.page.mytrainpage.click_add_training_button()
            #新建训练页点击添加训练
            self.page.addtrainpage.click_add_train_button()
            #断言
            assert self.page.addtrainpage.is_toast_exist("您还没有输入对小爱说的话哟~")
            return
        # 个人中心页点击我的训练
        self.page.centerpage.click_my_train()
        # 我的训练页点击添加训练
        self.page.mytrainpage.click_add_training_button()
        # 新建训练页点击添加训练
        self.page.addtrainpage.click_add_train_button()
        # 断言
        assert self.page.addtrainpage.is_toast_exist("您还没有输入对小爱说的话哟~")

    # 新建训练页面-你对小爱说的话“小爱同学”，点击添加训练，会有toast弹出
    def test_train02(self):
        # 首页点击个人中心按钮
        self.page.homepage.click_center_button()
        # 判断登录
        if self.page.centerpage.if_login():  # 登录：False,未登录：True
            # 未登录，点击登录
            self.page.centerpage.click_login_tab()
            self.page.loginpage.input_user("15527619642")
            self.page.loginpage.input_password("t1005033132")
            self.page.loginpage.click_login_button()
            time.sleep(3)
            # 个人中心页点击我的训练
            self.page.centerpage.click_my_train()
            # 我的训练页点击添加训练
            self.page.mytrainpage.click_add_training_button()
            # 新建训练页-你对小爱说的话“小爱同学”
            self.page.addtrainpage.input_train_request_box("小爱同学")
            # 新建训练页点击添加训练
            self.page.addtrainpage.click_add_train_button()
            # 断言
            assert self.page.addtrainpage.is_toast_exist("您还没有输入小爱的回应哟~")
            return
        # 个人中心页点击我的训练
        self.page.centerpage.click_my_train()
        # 我的训练页点击添加训练
        self.page.mytrainpage.click_add_training_button()
        # 新建训练页-你对小爱说的话“小爱同学”
        self.page.addtrainpage.input_train_request_box("小爱同学")
        # 新建训练页点击添加训练
        self.page.addtrainpage.click_add_train_button()
        # 断言
        assert self.page.addtrainpage.is_toast_exist("您还没有输入小爱的回应哟~")

    # 新建训练页面-小爱的回应 “在的”，点击添加训练，会有toast弹出
    def test_train03(self):
        # 首页点击个人中心按钮
        self.page.homepage.click_center_button()
        # 判断登录
        if self.page.centerpage.if_login():  # 登录：False,未登录：True
            # 未登录，点击登录
            self.page.centerpage.click_login_tab()
            self.page.loginpage.input_user("15527619642")
            self.page.loginpage.input_password("t1005033132")
            self.page.loginpage.click_login_button()
            time.sleep(3)
            # 个人中心页点击我的训练
            self.page.centerpage.click_my_train()
            # 我的训练页点击添加训练
            self.page.mytrainpage.click_add_training_button()
            # 新建训练页点击一句话
            self.page.addtrainpage.click_rerespone_one_word()
            # 新建训练页-小爱的回应 “在的”
            self.page.addtrainpage.input_train_reponse_box("在的")
            # 新建训练页点击添加训练
            self.page.addtrainpage.click_add_train_button()
            # 断言
            assert self.page.addtrainpage.is_toast_exist("您还没有输入对小爱说的话哟~")
            return
        # 个人中心页点击我的训练
        self.page.centerpage.click_my_train()
        # 我的训练页点击添加训练
        self.page.mytrainpage.click_add_training_button()
        # 新建训练页点击一句话
        self.page.addtrainpage.click_rerespone_one_word()
        # 新建训练页-小爱的回应 “在的”
        self.page.addtrainpage.input_train_reponse_box("在的")
        # 新建训练页点击添加训练
        self.page.addtrainpage.click_add_train_button()
        # 断言
        assert self.page.addtrainpage.is_toast_exist("您还没有输入对小爱说的话哟~")

    # 新建训练页面-正常添加一个小爱建议，跳转我的训练页
    def test_train04(self):
        # 首页点击个人中心按钮
        self.page.homepage.click_center_button()
        # 判断登录
        if self.page.centerpage.if_login():  # 登录：False,未登录：True
            # 未登录，点击登录
            self.page.centerpage.click_login_tab()
            self.page.loginpage.input_user("15527619642")
            self.page.loginpage.input_password("t1005033132")
            self.page.loginpage.click_login_button()
            time.sleep(3)
            # 个人中心页点击我的训练
            self.page.centerpage.click_my_train()
            # 我的训练页点击添加训练
            self.page.mytrainpage.click_add_training_button()
            # 新建训练页-你对小爱说的话“小爱同学”
            self.page.addtrainpage.input_train_request_box("小爱同学")
            # 新建训练页点击一句话
            self.page.addtrainpage.click_rerespone_one_word()
            # 新建训练页-小爱的回应 “在的”
            self.page.addtrainpage.input_train_reponse_box("在的")
            # 新建训练页点击添加训练
            self.page.addtrainpage.click_add_train_button()
            # 断言
            assert self.page.addtrainpage.is_toast_exist("已经存在")
            return
        # 个人中心页点击我的训练
        self.page.centerpage.click_my_train()
        # 我的训练页点击添加训练
        self.page.mytrainpage.click_add_training_button()
        # 新建训练页-你对小爱说的话“小爱同学”
        self.page.addtrainpage.input_train_request_box("小爱同学")
        # 新建训练页点击一句话
        self.page.addtrainpage.click_rerespone_one_word()
        # 新建训练页-小爱的回应 “当前时间戳”
        self.page.addtrainpage.input_train_reponse_box("在的")
        # 新建训练页点击添加训练
        self.page.addtrainpage.click_add_train_button()
        # 断言
        assert self.page.addtrainpage.is_toast_exist("已经存在")

# 8.23新增（何巧）
    # 个人中心页点击我的训练，新建一段录音的训练计划
    def test_click_addtrain05(self):
        # 首页点击个人中心按钮
        self.page.homepage.click_center_button()
        # 点击我的训练
        self.page.centerpage.click_my_train()
        # 点击我的训练-添加训练的按钮
        self.page.mytrainpage.click_add_training_button()
        # 新建训练-你对小爱说的话的输入框里面说话
        self.page.addtrainpage.input_train_request_box("同学")
        # 点击一段录音
        self.page.addtrainpage.click_onerecording()
        time.sleep(3)
        # 点击录音
        self.page.addtrainpage.click_soundrecording_button()
        # 暂停10秒，录音
        time.sleep(10)
        # 录音暂停
        self.page.addtrainpage.click_soundrecording_button()
        time.sleep(3)
        # 点击录音完成的按钮
        self.page.addtrainpage.click_record_done()
        # 点击添加训练的按钮
        self.page.addtrainpage.click_addtrain_button()
        assert self.page.addtrainpage.is_toast_exist("已经存在")


    # 个人中心页点击我的训练，点击设备控制，跳转页面
    def test_click_addtrain06(self):
        # 首页点击个人中心按钮
        self.page.homepage.click_center_button()
        # 点击我的训练
        self.page.centerpage.click_my_train()
        # 点击我的训练-添加训练的按钮
        self.page.mytrainpage.click_add_training_button()

        # 点击设备控制
        self.page.addtrainpage.click_equipmentcontrol()

        # 跳转页面

        assert self.page.addtrainpage.is_toast_exist("添加设备")


    # 编辑我的训练页面示例或者新建训练计划
    def test_click_addtrain07(self):
        # 首页点击个人中心按钮
        self.page.homepage.click_center_button()
        # 点击我的训练
        self.page.centerpage.click_my_train()
        time.sleep(2)
        # 点击我的训练-示例或者新建训练计划右上角的三个点
        self.page.addtrainpage.click_trainsetup()
        time.sleep(3)
        # print(self.driver.page_source)
        # print(self.page.addtrainpage.get_text(self.page.addtrainpage.edit_button))

        # 点击我的训练-示例或者新建训练计划右上角的三个点后-点击编辑
        self.page.addtrainpage.click_edit_button()

        assert self.page.addtrainpage.is_toast_exist("编辑训练")

    #删除我的训练页面示例或者新建训练计划
    def test_click_addtrain08(self):
        # 首页点击个人中心按钮
        self.page.homepage.click_center_button()
        # 点击我的训练
        self.page.centerpage.click_my_train()
        # 点击我的训练-示例或者新建训练计划右上角的三个点
        self.page.addtrainpage.click_trainsetup()
        # 点击我的训练-示例或者新建训练计划右上角的三个点后-点击删除
        self.page.addtrainpage.click_delect_button()
        # 弹框-确认
        self.page.addtrainpage.click_ok_button()

        assert self.page.addtrainpage.is_toast_exist("成功")

    #
    # 点击我的训练页面添加训练按钮-点击更多设置-跳转页面
    def test_click_addtrain09(self):
        # 首页点击个人中心按钮
        self.page.homepage.click_center_button()
        # 点击我的训练
        self.page.centerpage.click_my_train()
        #time.sleep(2)
        # 点击我的训练-添加训练的按钮
        self.page.mytrainpage.click_add_training_button()
        # 点击更多设置，
        self.page.addtrainpage.click_moresetup()
        # 断言，跳转的页面有全部执行
        assert self.page.addtrainpage.is_toast_exist("全部执行")


