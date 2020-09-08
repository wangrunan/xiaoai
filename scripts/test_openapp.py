#
# import time
#
# from base.driver import get_driver
# from page.page import Page
#
#
# class TestDomain:
#     def setup(self):
#         self.driver = get_driver()
#         self.page = Page(self.driver)
#
#     def teardown(self):
#         time.sleep(3)
#         self.driver.quit()
#
#     def test_open_app_01(self):
#         time.sleep(3)
#         # 首页点击键盘
#         self.page.homepage.click_keyboard()
#         # 对话页输入“打开计算器”
#         self.page.sessionpage.input_keyboard_input("打开计算器")
#         # 对话页点击发送
#         self.page.sessionpage.click_send_button()
#         time.sleep(3)
#         # 断言
#         # assert self.driver.current_activity == ".ScienceFragment"
#         assert self.driver.current_activity == ".Calculator"
#         # print(self.driver.current_activity)
#
#     #  query:打开照相机
#     def test_open_app_02(self):
#         time.sleep(3)
#         # 首页点击键盘
#         self.page.homepage.click_keyboard()
#         # 对话页输入“打开照相机”
#         self.page.sessionpage.input_keyboard_input("打开照相机")
#         # 对话页点击发送
#         self.page.sessionpage.click_send_button()
#         time.sleep(3)
#         # assert self.driver.current_activity == ".controller.CameraActivity"
#         print(self.driver.current_activity)
#         assert self.driver.current_activity == ".Camera"
#         # 断言
#         # print(self.driver.current_activity)
#
#     #  query:打开相册
#     def test_open_app_03(self):
#         time.sleep(3)
#         # 首页点击键盘
#         self.page.homepage.click_keyboard()
#         # 对话页输入“打开相册”
#         self.page.sessionpage.input_keyboard_input("打开相册")
#         # 对话页点击发送
#         self.page.sessionpage.click_send_button()
#         time.sleep(3)
#     #     # 断言
#         print(self.driver.current_activity)
#         time.sleep(5)
#         # assert self.driver.current_activity == ".presenter.main.MainTabActivity"
#         assert self.driver.current_activity =="com.oppo.gallery3d.app.Gallery"
#
#     #  query:打开设置
#     def test_open_app_04(self):
#         time.sleep(3)
#         # 首页点击键盘
#         self.page.homepage.click_keyboard()
#         # 对话页输入“打开设置”
#         self.page.sessionpage.input_keyboard_input("打开设置")
#         # 对话页点击发送
#         self.page.sessionpage.click_send_button()
#         print(self.driver.current_activity)
#         time.sleep(3)
#         # 断言
#
#         # assert self.driver.current_activity == " .presenter.main.MainTabActivity"
#
#     #  query:打开微信
#     def test_open_app_05(self):
#         time.sleep(3)
#         # 首页点击键盘
#         self.page.homepage.click_keyboard()
#         # 对话页输入“打开微信”
#         self.page.sessionpage.input_keyboard_input("打开微信")
#         # 对话页点击发送
#         self.page.sessionpage.click_send_button()
#         print(self.driver.current_activity)
#         time.sleep(3)
#         #断言
#         assert self.driver.current_activity == ".plugin.account.ui.LoginPasswordUI"
#
#     #  query:打开日历
#     def test_open_app_06(self):
#         time.sleep(3)
#         # 首页点击键盘
#         self.page.homepage.click_keyboard()
#         # 对话页输入“打开日历”
#         self.page.sessionpage.input_keyboard_input("打开日历")
#         # 对话页点击发送
#         self.page.sessionpage.click_send_button()
#         time.sleep(3)
#         print(self.driver.current_activity)
#         # 断言
#         assert self.driver.current_activity == ".AllInOneActivity"
#         # print(self.driver.current_activity)
#     #  query:打开地图  （已下载高德地图）
#     def test_open_app_07(self):
#         time.sleep(3)
#         # 首页点击键盘
#         self.page.homepage.click_keyboard()
#         # 对话页输入“打开地图”
#         self.page.sessionpage.input_keyboard_input("打开地图")
#         # 对话页点击发送
#         self.page.sessionpage.click_send_button()
#         time.sleep(3)
#         # 断言
#         assert self.driver.current_activity == "com.autonavi.map.activity.NewMapActivity"
#         # print(self.driver.current_activity)
#     #  query:打开微博（未安装微博）
#     def test_open_app_08(self):
#         time.sleep(3)
#         # 首页点击键盘
#         self.page.homepage.click_keyboard()
#         # 对话页输入“打开微博”
#         self.page.sessionpage.input_keyboard_input("打开微博")
#         # 对话页点击发送
#         self.page.sessionpage.click_send_button()
#         time.sleep(3)
#         # 断言
#         # assert "下载" in self.page.sessionpage.get_text(self.page.sessionpage.tts_reply)
#
#     #  query:打开文件管理
#     def test_open_app_09(self):
#         time.sleep(3)
#         # 首页点击键盘
#         self.page.homepage.click_keyboard()
#         # 对话页输入“打开文件”
#         self.page.sessionpage.input_keyboard_input("打开文件管理")
#         # 对话页点击发送
#         self.page.sessionpage.click_send_button()
#         time.sleep(3)
#         # 断言
#         assert self.driver.current_activity == ".Main"
#         # print(self.driver.current_activity)