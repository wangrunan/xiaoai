# import time
#
# from base.driver import get_driver
# from page.page import Page
#
#
# class TestLongPressSendQuery:
#     def setup(self):
#         self.driver = get_driver()
#         self.page = Page(self.driver)
#
#     def teardown(self):
#         time.sleep(3)
#         self.driver.quit()
#
#     # 长按用户query，点击复制
#     def  test_long_press_query(self):
#         time.sleep(3)
#         # 1.点击键盘
#         self.page.homepage.click_keyboard()
#         # 2.输入“今天天气”
#         self.page.sessionpage.input_keyboard_input("今天天气")
#         # 3.点击发送
#         self.page.sessionpage.click_send_button()
#         time.sleep(2)
#         # 4.点击返回
#         self.driver.press_keycode(4)
#         # 5.点击个人中心按钮
#         self.page.homepage.click_center_button()
#         # 6.点击对话记录按钮
#         self.page.centerpage.click_history_record()
#         # 7.长按query“今天天气”
#         self.page.historyrecordpage.long_press_query()
#         #点击复制
#         self.page.historyrecordpage.click_copy_button()
#         # 8.断言
#         assert self.page.historyrecordpage.is_toast_exist('已复制')
#         # assert self.page.historyrecordpage.is_copy_exist() and self.page.historyrecordpage.is_error_exist() and self.page.historyrecordpage.is_inform_exist()